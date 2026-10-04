r"""One-time: give the book's IAM user `awsbook` its CLI key, its console password and its MFA device, WITHOUT any secret
ever being printed or kept in a chat (the user's request of 2026-10-05 00:2x: "do this yourself").
    python bootstrap_user.py --admin-profile cicdbook
What it does, as the administrator profile:
  1. creates ONE access key for awsbook and writes it straight into the user's own ~/.aws/credentials as the section
     [awsbook] (replacing an older section of that name), and [profile awsbook] into ~/.aws/config (region us-east-1, json)
  2. makes a random 24-character console password, sets it with create-login-profile (no reset required), and stores it as
     the SecureString parameter /book-bootstrap/awsbook/console-password (Parameter Store, free; the author reads it in the
     console with "Show decrypted value" when a hand-taken picture needs a sign-in)
  3. creates a virtual MFA device named awsbook, enables it with two consecutive codes computed here from its seed, and
     stores the seed as the SecureString parameter /book-bootstrap/awsbook/mfa-seed (shots.py reads it to sign the screenshot
     browser in; the author can add the seed to an authenticator app from the console too)
  4. proves the profile answers as awsbook (prints the user name only)
Every secret lives only in the files and parameters named above. The script refuses to run twice (a key already exists).
"""
import base64, configparser, hashlib, hmac, json, os, secrets, string, struct, subprocess, sys, time
from pathlib import Path

AWS = r"C:\Program Files\Amazon\AWSCLIV2\aws.exe"
ADMIN = sys.argv[sys.argv.index("--admin-profile") + 1] if "--admin-profile" in sys.argv else "cicdbook"
USER = "awsbook"
REGION = "us-east-1"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def run(args, profile=ADMIN, check=True, stdin=None):
    r = subprocess.run([AWS, "--profile", profile, "--region", REGION, "--output", "json"] + args, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300, input=stdin)
    if check and r.returncode != 0:
        # an error message may echo an argument: print only the error code, never the text
        code = (r.stderr or "").split("(")[1].split(")")[0] if "(" in (r.stderr or "") else "error"
        sys.exit(f"aws {' '.join(args[:3])} failed: {code}")
    return json.loads(r.stdout) if (r.stdout or "").strip() else None


def totp(seed_b32, t=None):
    key = base64.b32decode(seed_b32.strip().upper() + "=" * (-len(seed_b32.strip()) % 8))
    counter = int((t if t is not None else time.time()) // 30)
    mac = hmac.new(key, struct.pack(">Q", counter), hashlib.sha1).digest()
    o = mac[-1] & 0x0F
    return f"{(struct.unpack('>I', mac[o:o + 4])[0] & 0x7FFFFFFF) % 1000000:06d}"


home_cfg = Path(os.environ.get("AWS_CONFIG_FILE") or (Path.home() / ".aws" / "config"))
home_cred = Path(os.environ.get("AWS_SHARED_CREDENTIALS_FILE") or (Path.home() / ".aws" / "credentials"))

# every step is skipped when it is already done, so a failed run can be repeated
cp = configparser.RawConfigParser(); cp.optionxform = str
if home_cred.exists():
    cp.read(home_cred, encoding="utf-8")
have_key = bool((run(["iam", "list-access-keys", "--user-name", USER]) or {}).get("AccessKeyMetadata"))
if have_key and cp.has_section(USER):
    print("1. access key exists and the credentials file has [awsbook]: kept")
elif have_key:
    sys.exit("awsbook has an access key but the credentials file has no [awsbook] section; delete the key in the console and rerun")
else:
    # 1. the access key, straight into the files
    ak = run(["iam", "create-access-key", "--user-name", USER])["AccessKey"]
    cp.add_section(USER)
    cp.set(USER, "aws_access_key_id", ak["AccessKeyId"])
    cp.set(USER, "aws_secret_access_key", ak["SecretAccessKey"])
    home_cred.parent.mkdir(parents=True, exist_ok=True)
    with open(home_cred, "w", encoding="utf-8", newline="\n") as f:
        cp.write(f, space_around_delimiters=True)
    del ak
    print("1. access key created and written to the credentials file as [awsbook]")
cfg = configparser.RawConfigParser(); cfg.optionxform = str
if home_cfg.exists():
    cfg.read(home_cfg, encoding="utf-8")
sect = f"profile {USER}"
if not cfg.has_section(sect):
    cfg.add_section(sect)
cfg.set(sect, "region", REGION); cfg.set(sect, "output", "json"); cfg.set(sect, "cli_pager", "")
with open(home_cfg, "w", encoding="utf-8", newline="\n") as f:
    cfg.write(f, space_around_delimiters=True)
print("   config has [profile awsbook]")

# 2. the console password (a fresh one every run that reaches here, so that the stored parameter always matches the profile)
alphabet = string.ascii_letters + string.digits + "!@#%^*-_=+"
pw = "".join(secrets.choice(alphabet) for _ in range(24))
r = subprocess.run([AWS, "--profile", ADMIN, "--region", REGION, "iam", "get-login-profile", "--user-name", USER], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
if r.returncode == 0:
    run(["iam", "update-login-profile", "--user-name", USER, "--password", pw, "--no-password-reset-required"])
else:
    run(["iam", "create-login-profile", "--user-name", USER, "--password", pw, "--no-password-reset-required"])
# Parameter Store reserves every name that starts with `aws` or `ssm` (measured 2026-10-05: "No access to reserved parameter
# name: awsbook-bootstrap/..."), so the book's parameters live under /book/...; the law only asks that the key be IN the name
run(["ssm", "put-parameter", "--name", "/book-bootstrap/awsbook/console-password", "--type", "SecureString", "--value", pw, "--overwrite",
     "--description", "the console password of the book's IAM user awsbook (bootstrap_user.py)"])
run(["ssm", "add-tags-to-resource", "--resource-type", "Parameter", "--resource-id", "/book-bootstrap/awsbook/console-password", "--tags", "Key=awsbook,Value=awsbook-bootstrap"], check=False)
del pw
print("2. console password set and stored as the SecureString parameter /book-bootstrap/awsbook/console-password")

# 3. the MFA device
if (run(["iam", "list-mfa-devices", "--user-name", USER]) or {}).get("MFADevices"):
    sys.exit("3. an MFA device is already enabled for awsbook; nothing more to do (the seed parameter must exist from the run that enabled it)")
tmp = Path(os.environ.get("TEMP", ".")) / f"awsbook-mfa-{secrets.token_hex(4)}.txt"
dev = run(["iam", "create-virtual-mfa-device", "--virtual-mfa-device-name", USER, "--outfile", str(tmp), "--bootstrap-method", "Base32StringSeed"])["VirtualMFADevice"]
seed = tmp.read_text(encoding="utf-8").strip()
tmp.unlink()
now = time.time()
c1, c2 = totp(seed, now - 30), totp(seed, now)
if c1 == c2:
    c2 = totp(seed, now + 30)
run(["iam", "enable-mfa-device", "--user-name", USER, "--serial-number", dev["SerialNumber"], "--authentication-code1", c1, "--authentication-code2", c2])
run(["ssm", "put-parameter", "--name", "/book-bootstrap/awsbook/mfa-seed", "--type", "SecureString", "--value", seed, "--overwrite",
     "--description", "the TOTP seed of the virtual MFA device of the book's IAM user awsbook (bootstrap_user.py); shots.py reads it to sign in"])
run(["ssm", "add-tags-to-resource", "--resource-type", "Parameter", "--resource-id", "/book-bootstrap/awsbook/mfa-seed", "--tags", "Key=awsbook,Value=awsbook-bootstrap"], check=False)
del seed, c1, c2
print("3. virtual MFA device awsbook created and enabled; its seed is the SecureString parameter /book-bootstrap/awsbook/mfa-seed")

# 4. the profile answers (IAM is eventually consistent: up to a minute)
for i in range(12):
    r = subprocess.run([AWS, "--profile", USER, "--region", REGION, "sts", "get-caller-identity", "--query", "Arn", "--output", "text"], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
    if r.returncode == 0 and (r.stdout or "").strip().endswith(f":user/{USER}"):
        print(f"4. the profile {USER} answers as the IAM user {(r.stdout or '').strip().rsplit('/', 1)[-1]} (after {i * 5} s)")
        break
    time.sleep(5)
else:
    sys.exit("the new key does not answer yet; try `aws sts get-caller-identity --profile awsbook` in a minute")
print("DONE. Nothing was printed but names.")
