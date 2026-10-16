# 20 - The compute catalogue - Batch, Lightsail, Outposts, Wavelength, WorkSpaces and the rest

The files the chapter **20 - The compute catalogue - Batch, Lightsail, Outposts, Wavelength, WorkSpaces and the rest** of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch20`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the section heading and the line where the file's text starts.

## What this chapter teaches

- Name the eight families of compute, say what each one hides from you, and tell Lambda, ECS, EKS and Lightsail apart in business words
- Opt in to a Local Zone group, read the Wavelength and Outposts catalogues, and choose between a Region, a Local Zone and an Outpost
- Run a Lightsail instance from the nginx blueprint with a static IP address, and say when Lightsail is the wrong answer
- Run AWS Batch jobs on Fargate: a compute environment, a queue, a job definition, one job and an array job that waits for it
- Walk the checklist for high performance computing and read which instance types support the Elastic Fabric Adapter
- Tell the WorkSpaces family apart and say why this account makes no desktop and no fleet
- Deploy a feature flag with AppConfig, sign a package with Signer, and read mail events, an IoT rule and a Lex bot
- Move data with AppFlow, publish a page with Amplify, use the tagging API, and make part of the catalogue as one CloudFormation stack

## Files

| File | Where it is in the chapter | Note |
|---|---|---|
| `catalogue.yaml` | Lightsail: servers with a fixed price › With CloudFormation (line 560) | the chapter adds to it in later blocks |
| `trust-ecs-tasks.json` | AWS Batch: jobs, queues and compute › With the CLI (line 650) |  |
| `jobdef.json` | AWS Batch: jobs, queues and compute › With the CLI (line 702) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `flags-v1.json` | Configuration and code trust: AppConfig and Signer › With the CLI (line 1282) |  |
| `flags-v2.json` | Configuration and code trust: AppConfig and Signer › With the CLI (line 1321) |  |
| `trust-iot.json` | Email, devices and conversations: SES, IoT Core, Lex and Connect › With the CLI (line 1608) |  |
| `iot-sqs.json` | Email, devices and conversations: SES, IoT Core, Lex and Connect › With the CLI (line 1612) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `rule.json` | Email, devices and conversations: SES, IoT Core, Lex and Connect › With the CLI (line 1628) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `trust-lex.json` | Email, devices and conversations: SES, IoT Core, Lex and Connect › With the CLI (line 1672) |  |
| `lex-polly.json` | Email, devices and conversations: SES, IoT Core, Lex and Connect › With the CLI (line 1676) |  |
| `people.csv` | Integration, hosting and console tools: AppFlow, Amplify, Tag Editor, CloudShell, Device Farm, Pinpoint and Ground Station › With the CLI (line 1904) | written with printf |
| `flow-bucket-policy.json` | Integration, hosting and console tools: AppFlow, Amplify, Tag Editor, CloudShell, Device Farm, Pinpoint and Ground Station › With the CLI (line 1918) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `tasks.json` | Integration, hosting and console tools: AppFlow, Amplify, Tag Editor, CloudShell, Device Farm, Pinpoint and Ground Station › With the CLI (line 1924) |  |
| `destinations.json` | Integration, hosting and console tools: AppFlow, Amplify, Tag Editor, CloudShell, Device Farm, Pinpoint and Ground Station › With the CLI (line 1929) | a template: the shell fills in $VARIABLES when the chapter runs it |
