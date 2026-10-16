# 12 - EC2 at architect level

The files the chapter **12 - EC2 at architect level** of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch12`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the section heading and the line where the file's text starts.

## What this chapter teaches

- Read the name of an instance type, and compare an Intel type with a Graviton type by their measured list prices
- Find a type with filters and with a list of requirements, and run one Arm instance for real
- Tell the private, the public and the Elastic address of an instance apart, and count against the quota of five
- Move a network interface from one instance to another and see its private address, its Elastic IP and its MAC address move with it
- Read the metadata service as a designer: the five options, the three levels, the account default and the five condition keys
- Push a key with EC2 Instance Connect, watch it expire after 60 seconds and find the push in CloudTrail
- Launch one Spot instance through an EC2 Fleet that draws from four pools, then delete the fleet
- Move an instance into a partition placement group and read its partition number from the inside

## Files

| File | Where it is in the chapter | Note |
|---|---|---|
| `cards.sh` | Network interfaces: the second card, the move and the failover › With the CLI (line 563) |  |
| `net-stack.yaml` | Network interfaces: the second card, the move and the failover › With CloudFormation (line 728) |  |
| `trust-ec2.json` | The metadata service at architect level › With the CLI (line 924) |  |
| `meta.sh` | The metadata service at architect level › With the CLI (line 1001) |  |
| `token.sh` | The metadata service at architect level › With the CLI (line 1069) |  |
| `off.sh` | The metadata service at architect level › With the CLI (line 1090) |  |
| `require-imdsv2.json` | The metadata service at architect level › With the CLI (line 1123) |  |
| `template-stack.yaml` | The metadata service at architect level › With CloudFormation (line 1229) |  |
| `eic-stack.yaml` | EC2 Instance Connect from the inside › With CloudFormation (line 1470) |  |
| `fleet.json` | EC2 Fleet: capacity across types and zones › With the CLI (line 1605) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `part.sh` | Placement, hibernate and recovery: the architect's reading › With the CLI (line 1789) |  |
| `ex-hops.json` | Try it yourself (line 2010) |  |
