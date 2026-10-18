# 20 - The catalogue, edge and hybrid compute, and Lightsail; AWS Batch, high performance computing and WorkSpaces; AppConfig and Signer, and email, devices and conversations; Integration and console tools, one stack, and cleaning up

The files the chapter **20**, in its parts **20.1 - The catalogue, edge and hybrid compute, and Lightsail**, **20.2 - AWS Batch, high performance computing and WorkSpaces**, **20.3 - AppConfig and Signer, and email, devices and conversations** and **20.4 - Integration and console tools, one stack, and cleaning up**, of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch20`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the part, the section heading and the line in that part where the file's text starts.

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
| `catalogue.yaml` | 20.1 › Lightsail: servers with a fixed price › With CloudFormation (line 563) | the chapter adds to it in later blocks |
| `trust-ecs-tasks.json` | 20.2 › AWS Batch: jobs, queues and compute › With the CLI (line 121) |  |
| `jobdef.json` | 20.2 › AWS Batch: jobs, queues and compute › With the CLI (line 170) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `flags-v1.json` | 20.3 › Configuration and code trust: AppConfig and Signer › With the CLI (line 105) |  |
| `flags-v2.json` | 20.3 › Configuration and code trust: AppConfig and Signer › With the CLI (line 142) |  |
| `trust-iot.json` | 20.3 › Email, devices and conversations: SES, IoT Core, Lex and Connect › With the CLI (line 441) |  |
| `iot-sqs.json` | 20.3 › Email, devices and conversations: SES, IoT Core, Lex and Connect › With the CLI (line 445) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `rule.json` | 20.3 › Email, devices and conversations: SES, IoT Core, Lex and Connect › With the CLI (line 460) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `trust-lex.json` | 20.3 › Email, devices and conversations: SES, IoT Core, Lex and Connect › With the CLI (line 506) |  |
| `lex-polly.json` | 20.3 › Email, devices and conversations: SES, IoT Core, Lex and Connect › With the CLI (line 510) |  |
| `people.csv` | 20.4 › Integration, hosting and console tools: AppFlow, Amplify, Tag Editor, CloudShell, Device Farm, Pinpoint and Ground Station › With the CLI (line 108) | written with printf |
| `flow-bucket-policy.json` | 20.4 › Integration, hosting and console tools: AppFlow, Amplify, Tag Editor, CloudShell, Device Farm, Pinpoint and Ground Station › With the CLI (line 121) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `tasks.json` | 20.4 › Integration, hosting and console tools: AppFlow, Amplify, Tag Editor, CloudShell, Device Farm, Pinpoint and Ground Station › With the CLI (line 127) |  |
| `destinations.json` | 20.4 › Integration, hosting and console tools: AppFlow, Amplify, Tag Editor, CloudShell, Device Farm, Pinpoint and Ground Station › With the CLI (line 132) | a template: the shell fills in $VARIABLES when the chapter runs it |
