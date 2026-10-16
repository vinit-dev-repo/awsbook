# 16 - Elastic Load Balancing

The files the chapter **16 - Elastic Load Balancing** of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch16`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the section heading and the line where the file's text starts.

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
| `user-data.sh` | Target groups and health checks › With the CLI (line 304) |  |
| `transform.json` | An Application Load Balancer and its listener rules › With the CLI (line 693) |  |
| `alb-stack.yaml` | An Application Load Balancer and its listener rules › With CloudFormation (line 762) |  |
| `log-policy.json` | Stickiness, cross-zone, headers, timeouts, logs and a zonal shift › With the CLI (line 1140) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `jwt-actions.json` | HTTPS at the load balancer › With the CLI (line 1512) |  |
| `nlb-stack.yaml` | A Network Load Balancer › With CloudFormation (line 1792) |  |
