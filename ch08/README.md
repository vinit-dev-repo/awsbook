# 08 - The CLI and the SDKs

The files the chapter **08 - The CLI and the SDKs** of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch08`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the section heading and the line where the file's text starts.

## What this chapter teaches

- Read the look-up order of the CLI, name a profile, and use `aws login`, IAM Identity Center or a role instead of a long-term key
- Pick an output format, then cut an answer down with `--query`, JMESPath, `--filters` and the paging options
- Read the return codes of the CLI and see Signature Version 4 at work with `--debug`
- Say what the CLI does when a call is throttled, and tell an API rate limit from a service quota
- Choose between your own terminal, CloudShell and Cloud9, which is closed to new customers
- Make, invoke, update and delete one Lambda function from the CLI, and make it again with a CloudFormation template
- Call the same function and S3 from Python with boto3, and see where boto3 finds its credentials
- Make a presigned URL, read its signature, then clean up and count `0`

## Files

| File | Where it is in the chapter | Note |
|---|---|---|
| `trust-lambda.json` | A Lambda function from the CLI › With the CLI (line 878) |  |
| `hello.py` | A Lambda function from the CLI › With the CLI (line 1006) | rewritten later in the chapter |
| `payload.json` | A Lambda function from the CLI › With the CLI (line 989) | written with echo |
| `fn-stack.yaml` | A Lambda function from the CLI › With CloudFormation (line 1071) |  |
| `list_regions.py` | The same work from an SDK: boto3 › With the CLI (line 1224) |  |
| `invoke.py` | The same work from an SDK: boto3 › With the CLI (line 1245) |  |
| `err.py` | The same work from an SDK: boto3 › With the CLI (line 1262) |  |
| `retries.py` | The same work from an SDK: boto3 › With the CLI (line 1282) |  |
| `note.txt` | S3 from the CLI and the SDK, and a presigned URL › With the CLI (line 1324) | written with echo |
| `s3_demo.py` | S3 from the CLI and the SDK, and a presigned URL › With the CLI (line 1359) |  |
| `bucket-stack.yaml` | S3 from the CLI and the SDK, and a presigned URL › With CloudFormation (line 1394) |  |
| `ex-fn-stack.yaml` | Try it yourself (line 1597) |  |
| `ex_invoke.py` | Try it yourself (line 1655) |  |
| `ex-note.txt` | Try it yourself (line 1673) | written with echo |
