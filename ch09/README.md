# 09 - Organizations, Control Tower, Identity Center and directories; Federation and Cognito; Identity at scale and cleaning up

The files the chapter **09**, in its parts **09.1 - Organizations, Control Tower, Identity Center and directories**, **09.2 - Federation and Cognito** and **09.3 - Identity at scale and cleaning up**, of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch09`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the part, the section heading and the line in that part where the file's text starts.

## What this chapter teaches

- Read an AWS Organization: its root, its organizational units, its accounts and its policy types
- Write service control policies, resource control policies and tag policies, and say how each one is inherited
- Say what AWS Control Tower, a landing zone and a control add on top of Organizations
- Explain IAM Identity Center, its two instance types, its permission sets and the AWS Builder ID
- Choose between AWS Managed Microsoft AD, AD Connector and Simple AD
- Say how federation trades proof from an identity provider for temporary credentials, and which kind fits which need
- Set up SAML 2.0 and OpenID Connect providers in IAM, and fix the common SAML errors
- Explain a custom identity broker and the calls it uses
- Sign app users in with a Cognito user pool, and read its tokens and its groups
- Trade a user pool token for AWS credentials with a Cognito identity pool, and choose its roles
- Delegate user creation with a permissions boundary, and test it with the policy simulator
- Use IAM Access Analyzer for findings, policy validation and custom policy checks, and know what each one costs
- Share resources with AWS RAM, and choose between a role and a resource policy for access across accounts
- Name the STS calls of the chapter side by side, and explain identity to a business owner in three sentences
- Make the chapter's identity resources in one CloudFormation stack, then clean up and count `0`

## Files

| File | Where it is in the chapter | Note |
|---|---|---|
| `deny-s3.json` | 09.1 › Organizations, organizational units and policies › With the CLI (line 430) |  |
| `saml-metadata.xml` | 09.2 › Federation into AWS: SAML, OIDC and identity brokers › With the CLI (line 211) |  |
| `trust-cognito.json` | 09.2 › Cognito identity pools › With the CLI (line 811) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `scp-deny-s3.json` | 09.3 › Identity at scale: boundaries, Access Analyzer, RAM and cross-account access › With the CLI (line 314) |  |
| `identity-stack.yaml` | 09.3 › Identity at scale: boundaries, Access Analyzer, RAM and cross-account access › With CloudFormation (line 417) |  |
| `ex-share.yaml` | 09.3 › Try it yourself (line 740) |  |
