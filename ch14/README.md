# 14 - Machine images

The files the chapter **14 - Machine images** of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch14`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the section heading and the line where the file's text starts.

## What this chapter teaches

- Say what an image holds, name the four places images come from, and find one with the console, `describe-images` or a public parameter
- Make an image from a running instance with a reboot and without one, and register an image from a snapshot
- Launch an instance from an image in another zone and see the same page come up
- Share an image with an account, see why a public share is refused, and keep the rules for encrypted images
- Copy an image to another Region with encryption
- Deprecate, disable and deregister an image, store one in S3, and write the policy that allows only approved images
- Build an image with an EC2 Image Builder pipeline: a component, a recipe, an infrastructure configuration, a distribution configuration and the pipeline

## Files

| File | Where it is in the chapter | Note |
|---|---|---|
| `user-data.sh` | Making an image: with a reboot, without a reboot, and from a snapshot › With the CLI (line 252) |  |
| `launch-stack.yaml` | Launching from an image and moving an instance between zones › With CloudFormation (line 444) |  |
| `approved-ami.json` | Retiring an image: deprecate, disable, deregister, the Recycle Bin and approved images › With the CLI (line 867) |  |
| `approved-ami-one.json` | Retiring an image: deprecate, disable, deregister, the Recycle Bin and approved images › With the CLI (line 901) |  |
| `trust-ec2.json` | EC2 Image Builder: a pipeline that builds, tests and distributes an image › With the CLI (line 1077) |  |
| `page-component.yaml` | EC2 Image Builder: a pipeline that builds, tests and distributes an image › With the CLI (line 1108) |  |
| `builder-stack.yaml` | EC2 Image Builder: a pipeline that builds, tests and distributes an image › With CloudFormation (line 1260) |  |
| `ex-component.yaml` | Try it yourself (line 1644) |  |
