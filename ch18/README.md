# 18 - What scales and survives, and a baseline that survives a zone; Scaling on the right signal and one plan for many resources; When it does not scale, the layers of a stack and cleaning up

The files the chapter **18**, in its parts **18.1 - What scales and survives, and a baseline that survives a zone**, **18.2 - Scaling on the right signal and one plan for many resources** and **18.3 - When it does not scale, the layers of a stack and cleaning up**, of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch18`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the part, the section heading and the line in that part where the file's text starts.

## What this chapter teaches

- Tell scalability from availability, and name the two ways to scale and the two kinds of high availability
- Build a small two-zone group behind a balancer and end an instance on purpose while a loop counts every answer
- Scale a group on requests per target and on the backlog of a queue, and say why other signals fail
- Run one scaling plan for a group, read the policy it made and delete it
- Find out why scaling did not happen: a failed launch, the maximum, an unhealthy target
- Read the quotas of the layers of a stack, and cache as far from the database as you can
- Delete everything in the right order and count that nothing is left

## Files

| File | Where it is in the chapter | Note |
|---|---|---|
| `trust-ec2.json` | 18.1 › The baseline that survives a zone › With the CLI (line 214) |  |
| `user-data.sh` | 18.1 › The baseline that survives a zone › With the CLI (line 284) |  |
| `lt.json` | 18.1 › The baseline that survives a zone › With the CLI (line 300) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `baseline-fragment.yaml` | 18.1 › The baseline that survives a zone › With CloudFormation (line 393) |  |
| `rq.json` | 18.2 › Scaling on the right signal › With the CLI (line 142) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `bl.json` | 18.2 › Scaling on the right signal › With the CLI (line 191) |  |
| `mm.json` | 18.2 › Scaling on the right signal › With the CLI (line 253) |  |
| `scaling-fragment.yaml` | 18.2 › Scaling on the right signal › With CloudFormation (line 296) |  |
| `plan.json` | 18.2 › One plan for many resources › With the CLI (line 379) |  |
| `plan-fragment.yaml` | 18.2 › One plan for many resources › With CloudFormation (line 432) |  |
| `alarm-fragment.yaml` | 18.3 › When it does not scale › With CloudFormation (line 295) |  |
