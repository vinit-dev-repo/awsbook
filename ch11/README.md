# 11 - Ways to pay, Spot Instances and placement groups; CPU credits, health checks, CloudWatch and changing an instance

The files the chapter **11**, in its parts **11.1 - Ways to pay, Spot Instances and placement groups** and **11.2 - CPU credits, health checks, CloudWatch and changing an instance**, of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch11`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the part, the section heading and the line in that part where the file's text starts.

## What this chapter teaches

- Name the seven ways to pay for EC2 and say which one fits which workload
- Read the offers, prices and counts for Reserved Instances, Dedicated Hosts and Capacity Reservations with the CLI
- Run a Spot Instance, read its request and avoid the trap of a cancelled request
- Make cluster, spread and partition placement groups and launch an instance into one
- Read CPU credits and switch a burstable instance between Standard and Unlimited mode
- Read the status checks, and make an alarm that recovers an instance
- Collect memory and disk numbers with the CloudWatch agent, and publish a custom metric
- Change the instance type, hibernate, reboot and clean up

## Files

| File | Where it is in the chapter | Note |
|---|---|---|
| `trust-ec2.json` | 11.1 › Placement groups: cluster, spread and partition › With the CLI (line 691) |  |
| `placement-stack.yaml` | 11.2 › Status checks, instance health and recovery › With CloudFormation (line 276) | rewritten later in the chapter |
| `cw-config.json` | 11.2 › CloudWatch for EC2: metrics, detailed monitoring, the agent and a custom metric › With the CLI (line 484) |  |
| `ex-stack.yaml` | 11.2 › Try it yourself (line 917) |  |
