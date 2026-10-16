# 13 - Instance storage - EBS and EFS

The files the chapter **13 - Instance storage - EBS and EFS** of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch13`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the section heading and the line where the file's text starts.

## What this chapter teaches

- Tell the three kinds of instance storage apart, name who looks after what, and read the root device of an instance
- Make, attach, format and mount an EBS volume, read the six volume types by their limits, and prove that a volume lives in one zone
- Grow a volume in place without a restart, and see the file system grow with it
- Take a snapshot, move a volume to another zone, keep snapshots with a lifecycle policy and bring a deleted snapshot back from the Recycle Bin
- Encrypt a volume, read the encryption default of a Region, and see why nobody wipes a volume by hand
- Share one io1 volume between two instances, and see why that needs a cluster-aware file system
- Prove that the instance store is empty after a stop
- Mount one EFS file system from two zones, through an access point, with a lifecycle policy and a backup policy

## Files

| File | Where it is in the chapter | Note |
|---|---|---|
| `ebs-stack.yaml` | EBS volumes: make, attach, format, mount › With CloudFormation (line 435) |  |
| `trust-dlm.json` | Snapshots: copies, moves, lifecycle and the Recycle Bin › With the CLI (line 733) |  |
| `dlm-policy.json` | Snapshots: copies, moves, lifecycle and the Recycle Bin › With the CLI (line 763) |  |
| `efs-stack.yaml` | EFS: one file system for many instances across zones › With CloudFormation (line 1452) |  |
