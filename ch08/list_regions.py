import boto3
ec2 = boto3.client("ec2")
names = sorted(r["RegionName"] for r in ec2.describe_regions()["Regions"])
print(len(names), "regions;", "first:", names[0], "last:", names[-1])
sts = boto3.client("sts")
print("caller:", sts.get_caller_identity()["Arn"].rsplit("/", 1)[-1])
