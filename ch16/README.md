# 16 - What a load balancer is, target groups and Application Load Balancer rules; Stickiness, headers, logs, zonal shift and HTTPS; Network and Gateway Load Balancers and cleaning up

The files the chapter **16**, in its parts **16.1 - What a load balancer is, target groups and Application Load Balancer rules**, **16.2 - Stickiness, headers, logs, zonal shift and HTTPS** and **16.3 - Network and Gateway Load Balancers and cleaning up**, of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch16`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the part, the section heading and the line in that part where the file's text starts.

## What this chapter teaches

- Say what a load balancer does, name the four kinds with their layers and years, and explain nodes, zones, cross-zone traffic and the security-group chain
- Make a target group with health checks, read the target states and reason codes, and set deregistration delay, routing algorithm and slow start
- Build an Application Load Balancer with rules of every condition and action kind, a weighted blue and green rule and a CloudFormation stack
- Measure sticky cookies, forwarded headers, access and connection logs and a zonal shift, and set the idle timeout
- End TLS at the balancer with an imported certificate, redirect HTTP to HTTPS, require a client certificate and add a Cognito sign-in rule
- Build a Network Load Balancer with an Elastic IP, proxy protocol version 2, an Application balancer as a target and a CloudFormation stack
- Make a Gateway Load Balancer and explain the endpoint, the route tables and the GENEVE path
- Choose the right front door for a web tier and clean up in the right order

## Files

| File | Where it is in the chapter | Note |
|---|---|---|
| `user-data.sh` | 16.1 › Target groups and health checks › With the CLI (line 341) |  |
| `transform.json` | 16.1 › An Application Load Balancer and its listener rules › With the CLI (line 744) |  |
| `alb-stack.yaml` | 16.1 › An Application Load Balancer and its listener rules › With CloudFormation (line 805) |  |
| `log-policy.json` | 16.2 › Stickiness, cross-zone, headers, timeouts, logs and a zonal shift › With the CLI (line 310) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `jwt-actions.json` | 16.2 › HTTPS at the load balancer › With the CLI (line 692) |  |
| `nlb-stack.yaml` | 16.3 › A Network Load Balancer › With CloudFormation (line 323) |  |
