import boto3
from botocore.exceptions import ClientError
lam = boto3.client("lambda")
try:
    lam.invoke(FunctionName="awsbook-ch08-missing")
except ClientError as e:
    print(e.response["Error"]["Code"])
