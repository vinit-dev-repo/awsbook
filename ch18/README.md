# 18 - High availability and scalability patterns

The files the chapter **18 - High availability and scalability patterns** of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch18`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the section heading and the line where the file's text starts.

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
| `trust-ec2.json` | The baseline that survives a zone › With the CLI (line 194) |  |
| `user-data.sh` | The baseline that survives a zone › With the CLI (line 264) |  |
| `lt.json` | The baseline that survives a zone › With the CLI (line 280) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `baseline-fragment.yaml` | The baseline that survives a zone › With CloudFormation (line 379) |  |
| `rq.json` | Scaling on the right signal › With the CLI (line 503) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `bl.json` | Scaling on the right signal › With the CLI (line 552) |  |
| `mm.json` | Scaling on the right signal › With the CLI (line 617) |  |
| `scaling-fragment.yaml` | Scaling on the right signal › With CloudFormation (line 668) |  |
| `plan.json` | One plan for many resources › With the CLI (line 740) |  |
| `plan-fragment.yaml` | One plan for many resources › With CloudFormation (line 800) |  |
| `alarm-fragment.yaml` | When it does not scale › With CloudFormation (line 1067) |  |
