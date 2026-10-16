# 17 - Auto Scaling Groups

The files the chapter **17 - Auto Scaling Groups** of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch17`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the section heading and the line where the file's text starts.

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
| `trust-ec2.json` | The launch template and the group behind the balancer › With the CLI (line 218) |  |
| `hook-policy.json` | The launch template and the group behind the balancer › With the CLI (line 223) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `hook-statement.json` | The launch template and the group behind the balancer › With the CLI (line 244) |  |
| `user-data.sh` | The launch template and the group behind the balancer › With the CLI (line 288) |  |
| `lt.json` | The launch template and the group behind the balancer › With the CLI (line 314) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `group-fragment.yaml` | The launch template and the group behind the balancer › With CloudFormation (line 437) |  |
| `tt.json` | Scaling policies › With the CLI (line 885) |  |
| `predictive.json` | Scaling policies › With the CLI (line 997) |  |
| `policies-fragment.yaml` | Scaling policies › With CloudFormation (line 1062) |  |
| `hooks-fragment.yaml` | Lifecycle hooks and notifications › With CloudFormation (line 1292) |  |
| `lt2.json` | Instance refresh › With the CLI (line 1400) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `refresh-fragment.yaml` | Instance refresh › With CloudFormation (line 1468) |  |
| `mixed.json` | Warm pools, mixed instances and Spot › With the CLI (line 1589) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `pool-fragment.yaml` | Warm pools, mixed instances and Spot › With CloudFormation (line 1658) |  |
| `asg-stack.yaml` | The stack with a rolling update › With the CLI (line 1731) |  |
| `ex-tt.json` | Try it yourself (line 2158) |  |
