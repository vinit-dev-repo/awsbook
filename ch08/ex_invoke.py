import boto3, json
lam = boto3.client("lambda")
r = lam.invoke(FunctionName="awsbook-ch08-ex-hello", Payload=json.dumps({"name": "exercise"}))
print(r["StatusCode"], json.loads(r["Payload"].read()))
