# awsbook

The files the chapters of the **AWS tutorial** (the LearnAIConcepts programme) write in their command blocks, one folder per chapter, extracted byte for byte from each certified chapter. Nothing here is meant to run on its own: read the chapter, which explains every line. Cloning a chapter's folder into the work folder the chapter names (`~/awsbook-chNN`) gives the same files the chapter's blocks would have typed.

## What the tutorial covers

The tutorial is one book in twelve parts and 117 chapters. Every service it covers is built for real, three ways: in the AWS Console with a picture of the real page, with the AWS CLI 2.36.40 in a block that runs on Windows (Git Bash) and on Ubuntu, and as a CloudFormation template once the book has introduced CloudFormation. Every block runs as the book's own IAM user `awsbook` in `us-east-1` (second region `ap-south-1`), and every resource a chapter creates is named `awsbook-chNN-...`, tagged `awsbook=awsbook-chNN` and deleted at the end of the chapter. Most chapters stay inside the AWS Free Tier; a chapter whose blocks leave it says so in its header with what one run costs.

A folder appears here when its chapter is certified (every command run three times on the final text, an independent critique applied). A chapter that is not listed below as present is still being written.

## Part I - AWS Foundations

| Folder | Chapter | Present |
|---|---|---|
| `ch01` | What cloud computing is | not yet |
| `ch02` | Getting started with an account | not yet |
| `ch03` | The AWS global infrastructure | not yet |
| `ch04` | The Well-Architected Framework - thinking like a cloud architect | not yet |
| `ch05` | The wider AWS service catalogue | not yet |
| `ch06` | IAM basics - users, groups, policies, MFA and the root user | not yet |
| `ch07` | IAM roles, policy evaluation and STS | not yet |
| `ch08` | The CLI and the SDKs | not yet |
| `ch09` | Advanced identity - Organizations, IAM Identity Center, Cognito and federation | not yet |

## Part II - AWS Compute

| Folder | Chapter | Present |
|---|---|---|
| `ch10` | EC2 basics - launching and reaching an instance | not yet |
| `ch11` | EC2 purchasing options, Spot, placement groups and instance health | not yet |
| `ch12` | EC2 at architect level | not yet |
| `ch13` | Instance storage - EBS and EFS | not yet |
| `ch14` | Machine images | not yet |
| `ch15` | Managing instances at scale with Systems Manager | not yet |
| `ch16` | Elastic Load Balancing | not yet |
| `ch17` | Auto Scaling Groups | not yet |
| `ch18` | High availability and scalability patterns | not yet |
| `ch19` | Elastic Beanstalk and the Spring Boot sample application | not yet |
| `ch20` | The compute catalogue - Batch, Lightsail, Outposts, Wavelength, WorkSpaces and the rest | not yet |

## Part III - Containers and Serverless on AWS

| Folder | Chapter | Present |
|---|---|---|
| `ch21` | Docker fundamentals (pointer to the Docker or Kubernetes module) | not yet |
| `ch22` | ECS clusters, task definitions and networking modes | not yet |
| `ch23` | ECS services, load balancing, auto scaling and logging | not yet |
| `ch24` | The container registry | not yet |
| `ch25` | Fargate | not yet |
| `ch26` | Kubernetes fundamentals (pointer to the Docker or Kubernetes module) | not yet |
| `ch27` | EKS - creating and running clusters | not yet |
| `ch28` | EKS storage and databases | not yet |
| `ch29` | EKS networking - the VPC CNI, Pod networking, security groups and network policies | not yet |
| `ch30` | The AWS Load Balancer Controller and Ingress on EKS | not yet |
| `ch31` | NLB with Kubernetes Services and ExternalDNS on EKS | not yet |
| `ch32` | EKS autoscaling | not yet |
| `ch33` | EKS security and workload identity | not yet |
| `ch34` | EKS observability | not yet |
| `ch35` | Microservices on EKS | not yet |
| `ch36` | Lambda functions - invocations, permissions, versions, layers and images | not yet |
| `ch37` | Lambda in an architecture - load balancers, URLs, VPC, EFS, performance and integrations | not yet |
| `ch38` | API Gateway | not yet |
| `ch39` | Step Functions and AppSync | not yet |
| `ch40` | SAM and the serverless frameworks | not yet |
| `ch41` | Serverless architecture and optimisation, and serverless compared with containers | not yet |

## Part IV - AWS Storage

| Folder | Chapter | Present |
|---|---|---|
| `ch42` | S3 fundamentals | not yet |
| `ch43` | Advanced S3 | not yet |
| `ch44` | S3 security | not yet |
| `ch45` | The wider storage catalogue | not yet |
| `ch46` | CloudFront basics - distributions, S3 origins, caching, invalidation and HTTPS | not yet |
| `ch47` | CloudFront advanced - origins, signed URLs, functions, encryption and logs | not yet |

## Part V - AWS Data Services

| Folder | Chapter | Present |
|---|---|---|
| `ch48` | RDS and Aurora | not yet |
| `ch49` | ElastiCache and caching | not yet |
| `ch50` | DynamoDB | not yet |
| `ch51` | The wider database catalogue | not yet |
| `ch52` | Data ingestion and storage | not yet |
| `ch53` | Transformation, integrity and feature engineering | not yet |
| `ch54` | Analytics services | not yet |

## Part VI - AWS Networking

| Folder | Chapter | Present |
|---|---|---|
| `ch55` | VPC fundamentals - CIDR, subnets, routes, gateways, security groups and NACLs | not yet |
| `ch56` | Reaching out of the VPC - NAT, bastion hosts, IPv6, IPAM and troubleshooting | not yet |
| `ch57` | Additional VPC features | not yet |
| `ch58` | DNS, DHCP and Route 53 | not yet |
| `ch59` | Network performance and optimisation | not yet |
| `ch60` | Traffic monitoring and troubleshooting | not yet |
| `ch61` | VPC peering, endpoints and PrivateLink | not yet |
| `ch62` | Transit Gateway and Cloud WAN | not yet |
| `ch63` | Site-to-Site VPN, Client VPN and BGP | not yet |
| `ch64` | Direct Connect - connections, virtual interfaces, the gateway, resiliency and encryption | not yet |
| `ch65` | VPC Lattice | not yet |
| `ch66` | Network security, management and governance | not yet |

## Part VII - AWS Application Integration

| Folder | Chapter | Present |
|---|---|---|
| `ch67` | SQS, SNS and Kinesis | not yet |
| `ch68` | Service communication patterns | not yet |

## Part VIII - AWS Infrastructure as Code and Delivery

| Folder | Chapter | Present |
|---|---|---|
| `ch69` | First templates - stacks, YAML, resources, parameters and mappings | not yet |
| `ch70` | Conditions, outputs, intrinsic functions, rules and resource policies | not yet |
| `ch71` | Metadata, cfn-init and the helper scripts | not yet |
| `ch72` | Nested stacks and StackSets | not yet |
| `ch73` | Deployment options, drift and stack policies | not yet |
| `ch74` | Advanced resources, macros and template generation | not yet |
| `ch75` | The Cloud Development Kit | not yet |
| `ch76` | Helm (pointer to the Docker or Kubernetes module) | not yet |
| `ch77` | Deployment and instance management at scale | not yet |
| `ch78` | CodeCommit, CodeBuild and CodeArtifact | not yet |
| `ch79` | CodeDeploy to EC2, Lambda and ECS | not yet |
| `ch80` | CodePipeline end to end - stages, approvals, notifications and CodeStar's successors | not yet |
| `ch81` | Pipelines that deploy to ECS and EKS | not yet |
| `ch82` | GitHub Actions against AWS | not yet |
| `ch83` | GitOps and Argo CD | not yet |
| `ch84` | SDLC automation | not yet |

## Part IX - AWS Operations

| Folder | Chapter | Present |
|---|---|---|
| `ch85` | CloudWatch - metrics, alarms, logs, dashboards and the agent | not yet |
| `ch86` | CloudTrail, Config, EventBridge for operations, the Health Dashboard and Service Quotas | not yet |
| `ch87` | X-Ray and distributed tracing | not yet |
| `ch88` | OpenTelemetry and managed observability | not yet |
| `ch89` | Disaster recovery and resilient architectures | not yet |
| `ch90` | Migrations | not yet |
| `ch91` | Incident and event response | not yet |
| `ch92` | Billing, budgets and account management | not yet |
| `ch93` | Reducing the bill | not yet |
| `ch94` | Cost control for architects | not yet |

## Part X - AWS Security

| Folder | Chapter | Present |
|---|---|---|
| `ch95` | Security, compliance and shared responsibility | not yet |
| `ch96` | Security governance | not yet |
| `ch97` | KMS, CloudHSM, Nitro Enclaves and Parameter Store | not yet |
| `ch98` | Certificates, Secrets Manager and data protection per service | not yet |
| `ch99` | Infrastructure security | not yet |
| `ch100` | Detection and threat findings | not yet |
| `ch101` | Security incident response | not yet |

## Part XI - AWS Machine Learning and Generative AI

| Folder | Chapter | Present |
|---|---|---|
| `ch102` | Managed AI services | not yet |
| `ch103` | SageMaker | not yet |
| `ch104` | The SageMaker built-in algorithms | not yet |
| `ch105` | Training, tuning and evaluating models | not yet |
| `ch106` | MLOps | not yet |
| `ch107` | Machine learning best practices | not yet |
| `ch108` | Generative AI fundamentals - transformers, tokens, embeddings and fine-tuning | not yet |
| `ch109` | Amazon Bedrock - models, the Converse API, Knowledge Bases, Guardrails and Agents | not yet |
| `ch110` | Prompt engineering | not yet |
| `ch111` | Managing data for generative AI | not yet |
| `ch112` | Agentic AI | not yet |
| `ch113` | Amazon Q and the AI developer tools | not yet |
| `ch114` | Governance, evaluation and responsible AI | not yet |
| `ch115` | Operational efficiency and optimisation | not yet |

## Part XII - AWS Certification

| Folder | Chapter | Present |
|---|---|---|
| `ch116` | Exam preparation and practice tests | not yet |
| `ch117` | Architecture discussions, scenarios and whitepapers | not yet |

## How the folders are made

Each chapter writes its files with `cat > FILE <<'EOF' ... EOF` blocks: CloudFormation templates, policy documents, Lambda code, task definitions, scripts. A tool reads the certified chapter and copies every such file here, under the chapter's folder, keeping the sub-folders the chapter's `cd` lines imply. Every folder has its own `README.md` listing its files. Nothing is hand-edited here; when a chapter changes, its folder is regenerated. No file here holds a key, a token, an account id or a password: the chapters create none, and a scan runs before every push.
