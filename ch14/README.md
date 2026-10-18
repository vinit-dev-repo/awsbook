# 14 - What an image is, making one and launching from it; Sharing, copying and retiring an image; EC2 Image Builder and cleaning up

The files the chapter **14**, in its parts **14.1 - What an image is, making one and launching from it**, **14.2 - Sharing, copying and retiring an image** and **14.3 - EC2 Image Builder and cleaning up**, of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch14`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the part, the section heading and the line in that part where the file's text starts.

## What this chapter teaches

- Say what an image holds, name the four places images come from, and find one with the console, `describe-images` or a public parameter
- Make an image from a running instance with a reboot and without one, and register an image from a snapshot
- Launch an instance from an image in another zone and see the same page come up
- Share an image with an account, see why a public share is refused, and keep the rules for encrypted images
- Copy an image to another Region with encryption
- Deprecate, disable and deregister an image, store one in S3, and write the policy that allows only approved images
- Build an image with an EC2 Image Builder pipeline: a component, a recipe, an infrastructure configuration, a distribution configuration and the pipeline
- Clean up in the reverse of the order of making, and count what is left down to 0

## Files

| File | Where it is in the chapter | Note |
|---|---|---|
| `user-data.sh` | 14.1 › Making an image: with a reboot, without a reboot, and from a snapshot › With the CLI (line 294) |  |
| `launch-stack.yaml` | 14.1 › Launching from an image and moving an instance between zones › With CloudFormation (line 496) |  |
| `approved-ami.json` | 14.2 › Retiring an image: deprecate, disable, deregister, the Recycle Bin and approved images › With the CLI (line 443) |  |
| `approved-ami-one.json` | 14.2 › Retiring an image: deprecate, disable, deregister, the Recycle Bin and approved images › With the CLI (line 477) |  |
| `trust-ec2.json` | 14.3 › EC2 Image Builder: a pipeline that builds, tests and distributes an image › With the CLI (line 196) |  |
| `page-component.yaml` | 14.3 › EC2 Image Builder: a pipeline that builds, tests and distributes an image › With the CLI (line 226) |  |
| `builder-stack.yaml` | 14.3 › EC2 Image Builder: a pipeline that builds, tests and distributes an image › With CloudFormation (line 382) |  |
| `ex-component.yaml` | 14.3 › Try it yourself (line 772) |  |
