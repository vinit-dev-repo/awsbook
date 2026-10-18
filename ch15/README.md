# 15 - What Systems Manager is, Run Command and Automation; Session Manager, State Manager and Patch Manager; Parameter Store, Distributor, OpsCenter and cleaning up

The files the chapter **15**, in its parts **15.1 - What Systems Manager is, Run Command and Automation**, **15.2 - Session Manager, State Manager and Patch Manager** and **15.3 - Parameter Store, Distributor, OpsCenter and cleaning up**, of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch15`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the part, the section heading and the line in that part where the file's text starts.

## What this chapter teaches

- Say what Systems Manager is, name its four tool groups and list what makes a node managed
- Run one command on many nodes by id, by tag and by resource group, and write a document of your own
- Restart an instance with an Automation runbook and explain the runbook that patches an image and updates an Auto Scaling group
- Open a session on a node that has no inbound port, set session preferences and name the endpoints that a private instance needs
- Keep nodes in a state with State Manager, collect an inventory and read compliance
- Patch nodes with a baseline and a patch group, and schedule the work with a maintenance window
- Store configuration in Parameter Store with a hierarchy, versions, labels and a SecureString
- Install a package with Distributor, track an issue in OpsCenter and register a server outside EC2 with a hybrid activation
- Clean up in the reverse of the order of making, and count what is left down to 0

## Files

| File | Where it is in the chapter | Note |
|---|---|---|
| `trust-ec2.json` | 15.1 › What Systems Manager is and what a managed node needs › With the CLI (line 182) |  |
| `trust-ssm.json` | 15.1 › What Systems Manager is and what a managed node needs › With the CLI (line 227) |  |
| `hello.yaml` | 15.1 › Run Command and documents › With the CLI (line 393) |  |
| `doc-stack.yaml` | 15.1 › Run Command and documents › With CloudFormation (line 544) |  |
| `prefs.json` | 15.2 › Session Manager › With the CLI (line 155) |  |
| `state-doc.yaml` | 15.2 › State Manager, Inventory and Compliance › With the CLI (line 304) |  |
| `assoc-stack.yaml` | 15.2 › State Manager, Inventory and Compliance › With CloudFormation (line 386) |  |
| `patching-stack.yaml` | 15.2 › Patch Manager and Maintenance Windows › With CloudFormation (line 641) |  |
| `param-stack.yaml` | 15.3 › Parameter Store › With CloudFormation (line 228) |  |
| `trust-hybrid.json` | 15.3 › Distributor, OpsCenter and nodes outside EC2 › With the CLI (line 434) |  |
| `ex-runbook.yaml` | 15.3 › Try it yourself (line 795) |  |
