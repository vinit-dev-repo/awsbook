import boto3, json
lam = boto3.client("lambda")
r = lam.invoke(FunctionName="awsbook-ch08-hello", Payload=json.dumps({"name": "boto3"}))
print(r["StatusCode"], json.loads(r["Payload"].read()))
