# 09 - Advanced identity - Organizations, IAM Identity Center, Cognito and federation

The files the chapter **09 - Advanced identity - Organizations, IAM Identity Center, Cognito and federation** of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch09`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the section heading and the line where the file's text starts.

## What this chapter teaches

- Read an AWS Organization: its root, its organizational units, its accounts and its policy types
- Write service control policies, resource control policies and tag policies, and say how each one is inherited
- Say what AWS Control Tower, a landing zone and a control add on top of Organizations
- Explain IAM Identity Center, its two instance types, its permission sets and the AWS Builder ID
- Choose between AWS Managed Microsoft AD, AD Connector and Simple AD
- Federate into AWS with SAML 2.0, OpenID Connect and a custom identity broker
- Sign app users in with a Cognito user pool, read its tokens, and trade a token for AWS credentials with an identity pool
- Delegate user creation with a permissions boundary, check access with IAM Access Analyzer, and share resources with AWS RAM

## Files

| File | Where it is in the chapter | Note |
|---|---|---|
| `deny-s3.json` | Organizations, organizational units and policies › With the CLI (line 358) |  |
| `saml-metadata.xml` | Federation into AWS: SAML, OIDC and identity brokers › With the CLI (line 815) |  |
| `trust-cognito.json` | Cognito identity pools › With the CLI (line 1311) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `scp-deny-s3.json` | Identity at scale: boundaries, Access Analyzer, RAM and cross-account access › With the CLI (line 1642) |  |
| `identity-stack.yaml` | Identity at scale: boundaries, Access Analyzer, RAM and cross-account access › With CloudFormation (line 1736) |  |
| `ex-share.yaml` | Try it yourself (line 2053) |  |
