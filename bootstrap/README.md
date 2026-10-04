# The book's one-time set-up

The AWS tutorial never works as your account's root user. It works as one IAM user named `awsbook`, which you make once with your own administrator sign-in. Everything the user may do is capped by a permissions boundary, and a monthly budget warns you by email.

`template.yaml` is a CloudFormation template that makes three things:

- the IAM user `awsbook`, with the boundary attached and no key, no password and no MFA device yet
- the managed policy `awsbook-permissions-boundary`, the most the user can ever do: it keeps the work in `us-east-1` and `ap-south-1`, refuses closing the account, changing contact or payment details and buying reservations, and lets the user make IAM users, roles and policies only under names that start with `awsbook-`
- the budget `awsbook-book-monthly-budget`, a cap in USD with alerts at 50, 80 and 100 percent and on a forecast above 100 percent

## Deploy it

Sign in to the AWS CLI as an administrator of your own account (`aws login`, or a profile of your own), then run from this folder's parent:

```bash
aws cloudformation deploy --region us-east-1 --stack-name awsbook-bootstrap --template-file bootstrap/template.yaml --capabilities CAPABILITY_NAMED_IAM --parameter-overrides AlertEmail=you@example.com MonthlyLimitUsd=40 --tags awsbook=awsbook-bootstrap
aws cloudformation describe-stacks --region us-east-1 --stack-name awsbook-bootstrap --query 'Stacks[0].StackStatus' --output text
```

Use your own email address for `AlertEmail`. AWS Budgets then sends that address a verification message. Open its link within 12 hours, signed in to this account, or the alerts never arrive.

## Give the user its credentials

Then open the console as the administrator, go to IAM, Users, `awsbook`, Security credentials, and create one access key for the CLI. Store it with `aws configure --profile awsbook`. The same tab lets you set a console password and add an MFA device.

`bootstrap_user.py` does the same three things from the command line, without any secret ever being printed: it writes the key straight into your `~/.aws/credentials` as the profile `awsbook`, sets a random console password and stores it in Parameter Store as a SecureString, and makes and enables a virtual MFA device whose seed it stores the same way. Run it once, as the administrator profile:

```bash
python bootstrap_user.py --admin-profile YOUR-ADMIN-PROFILE
```

It refuses to run twice.

## Remove it all

When you finish the book, delete the user's key, password and MFA device in the console, then delete the stack:

```bash
aws cloudformation delete-stack --region us-east-1 --stack-name awsbook-bootstrap
```
