# 06 - What IAM is, users, groups and policies; Keys, MFA, audits and the root user

The files the chapter **06**, in its parts **06.1 - What IAM is, users, groups and policies** and **06.2 - Keys, MFA, audits and the root user**, of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch06`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the part, the section heading and the line in that part where the file's text starts.

## What this chapter teaches

- Say what IAM does with one request, and tell identities, entities and principals apart
- Read an ARN, and find the account's numbers and quotas with the CLI
- Make a user under this book's permissions boundary with a console password, and see a user without the boundary refused
- Put users in a group and give the group a policy
- Write, read, version and test a customer managed policy and an inline policy, and read the simulator's three answers
- Make and rotate an access key, keep a key out of code and templates, and know where the CLI looks for credentials
- Give a user a virtual MFA device from the CLI, and name the kinds of device and the ways back in
- Read the password policy, the credential report and the last accessed data
- Make an IAM Access Analyzer for external access, and know what to do with a finding
- Guard the root user, and explain the IAM best practices and the shared responsibility to a non-technical owner

## Files

| File | Where it is in the chapter | Note |
|---|---|---|
| `team.yaml` | 06.1 › Users › With CloudFormation (line 306) |  |
| `list-buckets.json` | 06.1 › Policies › With the CLI (line 531) |  |
| `v2.json` | 06.1 › Policies › With the CLI (line 609) |  |
| `totp.py` | 06.2 › MFA on an IAM user › With the CLI (line 278) |  |
| `analyzer.yaml` | 06.2 › IAM Access Analyzer › With CloudFormation (line 574) |  |
