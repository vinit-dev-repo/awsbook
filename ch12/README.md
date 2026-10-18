# 12 - Instance types, addresses and network interfaces; The metadata service and EC2 Instance Connect; EC2 Fleet, placement groups and cleaning up

The files the chapter **12**, in its parts **12.1 - Instance types, addresses and network interfaces**, **12.2 - The metadata service and EC2 Instance Connect** and **12.3 - EC2 Fleet, placement groups and cleaning up**, of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch12`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the part, the section heading and the line in that part where the file's text starts.

## What this chapter teaches

- Read the name of an instance type, and compare an Intel type with a Graviton type by their measured list prices
- Find a type with filters and with a list of requirements, and run one Arm instance for real
- Tell the private, the public and the Elastic address of an instance apart, and count against the quota of five
- Move a network interface from one instance to another and see its private address, its Elastic IP and its MAC address move with it
- Read the metadata service as a designer: the five options, the three levels, the account default and the five condition keys
- Push a key with EC2 Instance Connect, watch it expire after 60 seconds and find the push in CloudTrail
- Lock the metadata settings with a policy and test it in the policy simulator
- Build a launch template and a security group rule with CloudFormation
- Launch one Spot instance through an EC2 Fleet that draws from four pools, then delete the fleet
- Move an instance into a partition placement group and read its partition number from the inside
- Clean up in the reverse of the order of making, and count what is left down to 0

## Files

| File | Where it is in the chapter | Note |
|---|---|---|
| `cards.sh` | 12.1 › Network interfaces: the second card, the move and the failover › With the CLI (line 628) |  |
| `net-stack.yaml` | 12.1 › Network interfaces: the second card, the move and the failover › With CloudFormation (line 800) |  |
| `trust-ec2.json` | 12.2 › The metadata service at architect level › With the CLI (line 166) |  |
| `meta.sh` | 12.2 › The metadata service at architect level › With the CLI (line 244) |  |
| `token.sh` | 12.2 › The metadata service at architect level › With the CLI (line 314) |  |
| `off.sh` | 12.2 › The metadata service at architect level › With the CLI (line 334) |  |
| `require-imdsv2.json` | 12.2 › The metadata service at architect level › With the CLI (line 371) |  |
| `template-stack.yaml` | 12.2 › The metadata service at architect level › With CloudFormation (line 479) |  |
| `eic-stack.yaml` | 12.2 › EC2 Instance Connect from the inside › With CloudFormation (line 726) |  |
| `fleet.json` | 12.3 › EC2 Fleet: capacity across types and zones › With the CLI (line 134) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `part.sh` | 12.3 › Placement, hibernate and recovery: the architect's reading › With the CLI (line 325) |  |
| `ex-hops.json` | 12.3 › Try it yourself (line 555) |  |
