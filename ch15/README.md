# 15 - Managing instances at scale with Systems Manager

The files the chapter **15 - Managing instances at scale with Systems Manager** of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch15`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the section heading and the line where the file's text starts.

## What this chapter teaches

- Say what Systems Manager is, name its four tool groups and list what makes a node managed
- Run one command on many nodes by id, by tag and by resource group, and write a document of your own
- Restart an instance with an Automation runbook and explain the runbook that patches an image and updates an Auto Scaling group
- Open a session on a node that has no inbound port, set session preferences and name the endpoints that a private instance needs
- Keep nodes in a state with State Manager, collect an inventory and read compliance
- Patch nodes with a baseline and a patch group, and schedule the work with a maintenance window
- Store configuration in Parameter Store with a hierarchy, versions, labels and a SecureString
- Install a package with Distributor, track an issue in OpsCenter and register a server outside EC2 with a hybrid activation

## Files

| File | Where it is in the chapter | Note |
|---|---|---|
| `trust-ec2.json` | What Systems Manager is and what a managed node needs › With the CLI (line 154) |  |
| `trust-ssm.json` | What Systems Manager is and what a managed node needs › With the CLI (line 197) |  |
| `hello.yaml` | Run Command and documents › With the CLI (line 350) |  |
| `doc-stack.yaml` | Run Command and documents › With CloudFormation (line 508) |  |
| `prefs.json` | Session Manager › With the CLI (line 792) |  |
| `state-doc.yaml` | State Manager, Inventory and Compliance › With the CLI (line 925) |  |
| `assoc-stack.yaml` | State Manager, Inventory and Compliance › With CloudFormation (line 1005) |  |
| `patching-stack.yaml` | Patch Manager and Maintenance Windows › With CloudFormation (line 1237) |  |
| `param-stack.yaml` | Parameter Store › With CloudFormation (line 1519) |  |
| `trust-hybrid.json` | Distributor, OpsCenter and nodes outside EC2 › With the CLI (line 1707) |  |
| `ex-runbook.yaml` | Try it yourself (line 2047) |  |
