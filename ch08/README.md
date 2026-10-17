# 08 - The CLI - profiles, output, queries, signing and retries; CloudShell, Lambda, Boto3 and a presigned URL

The files the chapter **08**, in its parts **08.1 - The CLI - profiles, output, queries, signing and retries** and **08.2 - CloudShell, Lambda, Boto3 and a presigned URL**, of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch08`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the part, the section heading and the line in that part where the file's text starts.

## What this chapter teaches

- Read the look-up order of the CLI, name a profile, and use `aws login`, IAM Identity Center or a role instead of a long-term key
- Pick an output format, and switch the pager off
- Cut an answer down with `--query`, JMESPath, `--filters` and the paging options
- Read the return codes of the CLI and see Signature Version 4 at work with `--debug`
- Say what the CLI does when a call is throttled, and tell an API rate limit from a service quota
- Choose between your own terminal, CloudShell and Cloud9, which is closed to new customers, and give a server a role instead of a key
- Make, invoke, update and delete one Lambda function from the CLI, and make it again with a CloudFormation template
- Hand a value to a command as shorthand, JSON, a file or a skeleton
- Call the same function and S3 from Python with Boto3, and see where Boto3 finds its credentials
- Make a presigned URL, read its parameters, then clean up and count `0`

## Files

| File | Where it is in the chapter | Note |
|---|---|---|
| `trust-lambda.json` | 08.2 › A Lambda function from the CLI › With the CLI (line 254) |  |
| `hello.py` | 08.2 › A Lambda function from the CLI › With the CLI (line 378) | rewritten later in the chapter |
| `payload.json` | 08.2 › A Lambda function from the CLI › With the CLI (line 362) | written with echo |
| `fn-stack.yaml` | 08.2 › A Lambda function from the CLI › With CloudFormation (line 442) |  |
| `list_regions.py` | 08.2 › The same work from an SDK: boto3 › With the CLI (line 608) |  |
| `invoke.py` | 08.2 › The same work from an SDK: boto3 › With the CLI (line 628) |  |
| `err.py` | 08.2 › The same work from an SDK: boto3 › With the CLI (line 644) |  |
| `retries.py` | 08.2 › The same work from an SDK: boto3 › With the CLI (line 663) |  |
| `note.txt` | 08.2 › S3 from the CLI and the SDK, and a presigned URL › With the CLI (line 727) | written with echo |
| `s3_demo.py` | 08.2 › S3 from the CLI and the SDK, and a presigned URL › With the CLI (line 762) |  |
| `bucket-stack.yaml` | 08.2 › S3 from the CLI and the SDK, and a presigned URL › With CloudFormation (line 793) |  |
| `ex-fn-stack.yaml` | 08.2 › Try it yourself (line 1000) |  |
| `ex_invoke.py` | 08.2 › Try it yourself (line 1058) |  |
| `ex-note.txt` | 08.2 › Try it yourself (line 1076) | written with echo |
