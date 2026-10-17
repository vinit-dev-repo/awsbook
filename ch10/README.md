# 10 - What EC2 is, the pieces of a launch and a first instance; Reaching the instance, its metadata and its addresses; Images, the life of an instance and cleaning up

The files the chapter **10**, in its parts **10.1 - What EC2 is, the pieces of a launch and a first instance**, **10.2 - Reaching the instance, its metadata and its addresses** and **10.3 - Images, the life of an instance and cleaning up**, of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch10`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the part, the section heading and the line in that part where the file's text starts.

## What this chapter teaches

- Name the parts of an instance and its states, and say what one hour of a `t3.micro` costs at list price
- Find the default VPC, the latest Amazon Linux 2023 image and a free-tier instance type with the CLI
- Make a key pair and a security group that opens port 22 to your own address and port 80 to anyone
- Launch one web server three ways: the CLI, the console and a CloudFormation stack
- Reach an instance with SSH, EC2 Instance Connect and an EC2 Instance Connect Endpoint
- Read the connection errors and tell which side to look at
- Read the metadata service with IMDSv2, and give an instance a role instead of a key
- Keep an address with an Elastic IP, and attach a second network interface
- Make an image of an instance, and end it with two calls
- Say what a reboot, a stop and start, a hibernate and a terminate keep
- Read the end-of-life settings, and switch termination protection on and off
- Clean up in reverse order and count `0`

## Files

| File | Where it is in the chapter | Note |
|---|---|---|
| `user-data.sh` | 10.1 › Launching an instance: the CLI, the console and a stack › With the CLI (line 494) |  |
| `web-stack.yaml` | 10.1 › Launching an instance: the CLI, the console and a stack › With CloudFormation (line 588) |  |
| `eice-stack.yaml` | 10.2 › Reaching the instance: SSH, Instance Connect and the endpoint › With CloudFormation (line 335) |  |
| `trust-ec2.json` | 10.2 › Inside the instance: the metadata service, user data and the instance role › With the CLI (line 505) |  |
| `on-instance.sh` | 10.2 › Inside the instance: the metadata service, user data and the instance role › With the CLI (line 559) |  |
| `role-stack.yaml` | 10.2 › Inside the instance: the metadata service, user data and the instance role › With CloudFormation (line 587) |  |
| `net-stack.yaml` | 10.2 › Addresses and interfaces: public, Elastic and a second card › With CloudFormation (line 841) |  |
| `ex-user-data.sh` | 10.3 › Try it yourself (line 408) |  |
| `ex-meta.sh` | 10.3 › Try it yourself (line 473) |  |
