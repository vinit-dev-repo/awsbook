# 06 - IAM basics - users, groups, policies, MFA and the root user

The files the chapter **06 - IAM basics - users, groups, policies, MFA and the root user** of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch06`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the section heading and the line where the file's text starts.

## What this chapter teaches

- Say what IAM does with one request, and tell identities, entities and principals apart
- Make a user with a console password, an access key and a virtual MFA device, under this book's permissions boundary
- Put users in a group and give the group a policy, then write, read and test a customer managed policy and an inline policy
- Use the policy simulator to see the three answers: allowed, explicit deny and implicit deny
- Rotate an access key, set up the CLI as a user, and keep a key out of code and templates
- Read the password policy, the credential report and the last accessed data, and make an IAM Access Analyzer for external access
- Guard the root user, and explain the IAM best practices and the shared responsibility to a non-technical owner

## Files

| File | Where it is in the chapter | Note |
|---|---|---|
| `team.yaml` | Users › With CloudFormation (line 255) |  |
| `list-buckets.json` | Policies › With the CLI (line 442) |  |
| `v2.json` | Policies › With the CLI (line 526) |  |
| `totp.py` | MFA on an IAM user › With the CLI (line 776) |  |
| `analyzer.yaml` | IAM Access Analyzer › With CloudFormation (line 1039) |  |
