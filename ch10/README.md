# 10 - EC2 basics - launching and reaching an instance

The files the chapter **10 - EC2 basics - launching and reaching an instance** of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch10`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the section heading and the line where the file's text starts.

## What this chapter teaches

- Name the parts of an instance, and say what one hour of a `t3.micro` costs at list price
- Find the default VPC, the latest Amazon Linux 2023 image and a free-tier instance type with the CLI
- Make a key pair and a security group that opens port 22 to your own address and port 80 to anyone
- Launch one web server three ways: the CLI, the console and a CloudFormation stack
- Reach an instance with SSH, EC2 Instance Connect and an EC2 Instance Connect Endpoint, and read the three connection errors
- Read the metadata service with IMDSv2, and give an instance a role instead of a key
- Keep an address with an Elastic IP, attach a second network interface and make an image of an instance
- Stop, start, reboot and terminate an instance, then clean up and count `0`

## Files

| File | Where it is in the chapter | Note |
|---|---|---|
| `user-data.sh` | Launching an instance: the CLI, the console and a stack › With the CLI (line 414) |  |
| `web-stack.yaml` | Launching an instance: the CLI, the console and a stack › With CloudFormation (line 506) |  |
| `eice-stack.yaml` | Reaching the instance: SSH, Instance Connect and the endpoint › With CloudFormation (line 914) |  |
| `trust-ec2.json` | Inside the instance: the metadata service, user data and the instance role › With the CLI (line 1069) |  |
| `on-instance.sh` | Inside the instance: the metadata service, user data and the instance role › With the CLI (line 1122) |  |
| `role-stack.yaml` | Inside the instance: the metadata service, user data and the instance role › With CloudFormation (line 1152) |  |
| `net-stack.yaml` | Addresses and interfaces: public, Elastic and a second card › With CloudFormation (line 1390) |  |
| `ex-user-data.sh` | Try it yourself (line 1795) |  |
| `ex-meta.sh` | Try it yourself (line 1860) |  |
