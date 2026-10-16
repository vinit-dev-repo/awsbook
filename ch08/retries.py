import boto3
from botocore.config import Config
cfg = Config(retries={"mode": "standard", "total_max_attempts": 5})
sts = boto3.client("sts", config=cfg)
print(sts.get_caller_identity()["ResponseMetadata"]["RetryAttempts"])
