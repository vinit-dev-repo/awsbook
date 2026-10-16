# 07 - IAM roles, policy evaluation and STS

The files the chapter **07 - IAM roles, policy evaluation and STS** of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch07`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the section heading and the line where the file's text starts.

## What this chapter teaches

- Say what an IAM role is, what its trust policy and its permissions policy do, and who may assume it
- Assume a role with STS, read the three temporary credentials, and set how long a session lasts
- Close the confused deputy gap with an external id, and tell the STS calls and endpoints apart
- Read a policy element by element: Action and NotAction, Principal, Condition operators, global keys and variables
- Follow one request through the evaluation logic and prove each layer with the policy simulator
- Use tags to grant access (ABAC), make roles for services, and control who may pass a role
- Revoke the sessions of a role, and give a server outside AWS credentials with IAM Roles Anywhere
- Make a role with the console, with the CLI and with a CloudFormation template

## Files

| File | Where it is in the chapter | Note |
|---|---|---|
| `trust.json` | What a role is › With the CLI (line 84) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `trust-ext.json` | The confused deputy and the external id › With the CLI (line 347) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `trust-lambda.json` | Roles for services, PassRole and instance profiles › With the CLI (line 753) |  |
| `roles-stack.yaml` | Roles for services, PassRole and instance profiles › With CloudFormation (line 818) |  |
| `trust-ra.json` | IAM Roles Anywhere › With the CLI (line 1066) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `ra-stack.yaml` | IAM Roles Anywhere › With CloudFormation (line 1105) |  |
| `trust-ex.json` | Try it yourself (line 1263) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `ec2-stack.yaml` | Try it yourself (line 1306) |  |
