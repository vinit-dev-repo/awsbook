import boto3
s3 = boto3.client("s3")
print("buckets:", len([b for b in s3.list_buckets()["Buckets"] if b["Name"].startswith("awsbook-ch08")]))
s3.put_object(Bucket="awsbook-ch08-files", Key="sdk-note.txt", Body="written by boto3")
body = s3.get_object(Bucket="awsbook-ch08-files", Key="sdk-note.txt")["Body"].read().decode()
print(body)
