# 17 - What a group is, the group behind a balancer and keeping it healthy; Scaling policies and lifecycle hooks; Instance refresh, warm pools, a rolling update and cleaning up

The files the chapter **17**, in its parts **17.1 - What a group is, the group behind a balancer and keeping it healthy**, **17.2 - Scaling policies and lifecycle hooks** and **17.3 - Instance refresh, warm pools, a rolling update and cleaning up**, of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch17`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the part, the section heading and the line in that part where the file's text starts.

## What this chapter teaches

- Say what an Auto Scaling group is, read its three sizes, follow an instance through its lifecycle states and read what one run costs
- Build a launch template and a group behind an Application Load Balancer, with ELB health checks, a warmup and group metrics
- Replace an instance, scale by hand, use standby and scale-in protection, suspend processes and read the termination order
- Scale with a target tracking policy under a real load, with step and simple policies, with schedules and with a forecast
- Hold instances with launch and terminate lifecycle hooks, and send the events to a topic and to an EventBridge rule
- Roll a new launch template version through a group with an instance refresh, and choose among the three update strategies
- Add a warm pool, run a mixed Spot group and update a group in a CloudFormation stack with a rolling update
- Delete everything in the right order and count that nothing is left

## Files

| File | Where it is in the chapter | Note |
|---|---|---|
| `trust-ec2.json` | 17.1 › The launch template and the group behind the balancer › With the CLI (line 239) |  |
| `hook-policy.json` | 17.1 › The launch template and the group behind the balancer › With the CLI (line 244) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `hook-statement.json` | 17.1 › The launch template and the group behind the balancer › With the CLI (line 264) |  |
| `user-data.sh` | 17.1 › The launch template and the group behind the balancer › With the CLI (line 307) |  |
| `lt.json` | 17.1 › The launch template and the group behind the balancer › With the CLI (line 333) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `group-fragment.yaml` | 17.1 › The launch template and the group behind the balancer › With CloudFormation (line 452) |  |
| `tt.json` | 17.2 › Scaling policies › With the CLI (line 212) |  |
| `predictive.json` | 17.2 › Scaling policies › With the CLI (line 326) |  |
| `policies-fragment.yaml` | 17.2 › Scaling policies › With CloudFormation (line 382) |  |
| `hooks-fragment.yaml` | 17.2 › Lifecycle hooks and notifications › With CloudFormation (line 623) |  |
| `lt2.json` | 17.3 › Instance refresh › With the CLI (line 128) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `refresh-fragment.yaml` | 17.3 › Instance refresh › With CloudFormation (line 191) |  |
| `mixed.json` | 17.3 › Warm pools, mixed instances and Spot › With the CLI (line 328) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `pool-fragment.yaml` | 17.3 › Warm pools, mixed instances and Spot › With CloudFormation (line 389) |  |
| `asg-stack.yaml` | 17.3 › The stack with a rolling update › With the CLI (line 474) |  |
| `ex-tt.json` | 17.3 › Try it yourself (line 891) |  |
