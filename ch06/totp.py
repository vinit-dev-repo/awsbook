import base64, hashlib, hmac, struct, sys, time
seed = open(sys.argv[1]).read().strip()
key = base64.b32decode(seed.upper() + "=" * (-len(seed) % 8))
def code(t):
    mac = hmac.new(key, struct.pack(">Q", int(t // 30)), hashlib.sha1).digest()
    o = mac[-1] & 15
    return "%06d" % ((struct.unpack(">I", mac[o:o + 4])[0] & 0x7FFFFFFF) % 1000000)
print(code(time.time() - 30), code(time.time()))
