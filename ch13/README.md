# 13 - Storage kinds, EBS volumes and Elastic Volumes; Snapshots, encryption and Multi-Attach; The instance store, EFS and cleaning up

The files the chapter **13**, in its parts **13.1 - Storage kinds, EBS volumes and Elastic Volumes**, **13.2 - Snapshots, encryption and Multi-Attach** and **13.3 - The instance store, EFS and cleaning up**, of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch13`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the part, the section heading and the line in that part where the file's text starts.

## What this chapter teaches

- Tell the three kinds of instance storage apart, name who looks after what, and read the root device of an instance
- Make, attach, format and mount an EBS volume, read the six volume types by their limits, and prove that a volume lives in one zone
- Grow a volume in place without a restart, and see the file system grow with it
- Take a snapshot, move a volume to another zone, keep snapshots with a lifecycle policy and bring a deleted snapshot back from the Recycle Bin
- Encrypt a volume, read the encryption default of a Region, and see why nobody wipes a volume by hand
- Share one io1 volume between two instances, and see why that needs a cluster-aware file system
- Prove that the instance store is empty after a stop
- Mount one EFS file system from two zones, through an access point, with a lifecycle policy and a backup policy
- Clean up in the reverse of the order of making, and count what is left down to 0

## Files

| File | Where it is in the chapter | Note |
|---|---|---|
| `ebs-stack.yaml` | 13.1 › EBS volumes: make, attach, format, mount › With CloudFormation (line 502) |  |
| `trust-dlm.json` | 13.2 › Snapshots: copies, moves, lifecycle and the Recycle Bin › With the CLI (line 207) |  |
| `dlm-policy.json` | 13.2 › Snapshots: copies, moves, lifecycle and the Recycle Bin › With the CLI (line 236) |  |
| `efs-stack.yaml` | 13.3 › EFS: one file system for many instances across zones › With CloudFormation (line 483) |  |
