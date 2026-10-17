# 07 - Roles, STS and the policy language; Tags, service roles, revoking sessions and Roles Anywhere

The files the chapter **07**, in its parts **07.1 - Roles, STS and the policy language** and **07.2 - Tags, service roles, revoking sessions and Roles Anywhere**, of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch07`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the part, the section heading and the line in that part where the file's text starts.

## What this chapter teaches

- Say what an IAM role is, what its trust policy and its permissions policy do, and who may assume it
- Assume a role with STS, read the three temporary credentials, and set how long a session lasts
- Close the confused deputy gap with an external id, and tell the STS calls and endpoints apart
- Read a policy element by element: Action and NotAction, Principal, Condition operators, global keys and variables
- Follow one request through the evaluation logic, and prove each layer with the policy simulator
- Use tags to grant access (ABAC), with principal, resource, request and session tags
- Make a role for a service, and control who may pass a role with `iam:PassRole`
- Tell an instance profile, the instance metadata and the two ECS roles apart
- Revoke the sessions of a role, and stop one principal or one session
- Give a server outside AWS credentials with IAM Roles Anywhere, and make a role with a CloudFormation template

## Files

| File | Where it is in the chapter | Note |
|---|---|---|
| `trust.json` | 07.1 › What a role is › With the CLI (line 90) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `trust-ext.json` | 07.1 › The confused deputy and the external id › With the CLI (line 386) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `trust-lambda.json` | 07.2 › Roles for services, PassRole and instance profiles › With the CLI (line 186) |  |
| `roles-stack.yaml` | 07.2 › Roles for services, PassRole and instance profiles › With CloudFormation (line 244) |  |
| `trust-ra.json` | 07.2 › IAM Roles Anywhere › With the CLI (line 520) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `ra-stack.yaml` | 07.2 › IAM Roles Anywhere › With CloudFormation (line 557) |  |
| `trust-ex.json` | 07.2 › Try it yourself (line 718) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `ec2-stack.yaml` | 07.2 › Try it yourself (line 761) |  |
