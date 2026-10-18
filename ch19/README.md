# 19 - What Elastic Beanstalk is and the sample application; The first environment, its configuration and an all-at-once deployment; The database, the production environment and safe deployments; Swaps, the worker tier and cleaning up

The files the chapter **19**, in its parts **19.1 - What Elastic Beanstalk is and the sample application**, **19.2 - The first environment, its configuration and an all-at-once deployment**, **19.3 - The database, the production environment and safe deployments** and **19.4 - Swaps, the worker tier and cleaning up**, of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch19`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the part, the section heading and the line in that part where the file's text starts.

## What this chapter teaches

- Name the parts of Elastic Beanstalk: application, version, environment, tier, platform and configuration, and say what it makes for you
- Build and test two Spring Boot services on your own machine and run them against one Postgres container
- Deploy the movie service to a single-instance environment with a database that Beanstalk couples to it
- Change a setting, read the logs, and deploy a new version all at once while a loop counts the failed requests
- Decouple the database and keep it, then give a second environment the same database through a parameter
- Make a load-balanced production environment with CloudFormation and deploy to it with the immutable and traffic-splitting policies
- Swap the names of two environments, and read how cloning, managed updates and the Cluster mode work
- Run a worker environment that reads a queue, then delete everything in the right order

## Files

| File | Where it is in the chapter | Note |
|---|---|---|
| `movie-service/pom.xml` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 297) |  |
| `movie-service/Dockerfile` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 370) |  |
| `movie-service/src/main/resources/application.properties` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 377) |  |
| `movie-service/src/main/resources/schema.sql` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 384) |  |
| `movie-service/src/main/resources/data.sql` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 392) |  |
| `movie-service/src/main/java/com/awsbook/movie/MovieServiceApplication.java` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 409) |  |
| `movie-service/src/main/java/com/awsbook/movie/Genre.java` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 422) |  |
| `movie-service/src/main/java/com/awsbook/movie/MovieDto.java` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 427) |  |
| `movie-service/src/main/java/com/awsbook/movie/Movie.java` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 432) |  |
| `movie-service/src/main/java/com/awsbook/movie/MovieRepository.java` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 454) |  |
| `movie-service/src/main/java/com/awsbook/movie/MovieController.java` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 464) |  |
| `movie-service/src/main/java/com/awsbook/movie/VersionController.java` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 493) |  |
| `movie-service/src/test/java/com/awsbook/movie/TestContainersConfiguration.java` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 515) |  |
| `movie-service/src/test/java/com/awsbook/movie/MovieServiceApplicationTests.java` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 534) |  |
| `customer-service/pom.xml` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 588) |  |
| `customer-service/Dockerfile` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 665) |  |
| `customer-service/src/main/resources/application.properties` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 672) |  |
| `customer-service/src/main/resources/schema.sql` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 680) |  |
| `customer-service/src/main/resources/data.sql` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 687) |  |
| `customer-service/src/main/java/com/awsbook/customer/CustomerServiceApplication.java` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 697) |  |
| `customer-service/src/main/java/com/awsbook/customer/Genre.java` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 710) |  |
| `customer-service/src/main/java/com/awsbook/customer/MovieDto.java` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 715) |  |
| `customer-service/src/main/java/com/awsbook/customer/CustomerDto.java` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 720) |  |
| `customer-service/src/main/java/com/awsbook/customer/GenreUpdateRequest.java` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 727) |  |
| `customer-service/src/main/java/com/awsbook/customer/Customer.java` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 732) |  |
| `customer-service/src/main/java/com/awsbook/customer/CustomerRepository.java` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 762) |  |
| `customer-service/src/main/java/com/awsbook/customer/CustomerNotFoundException.java` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 769) |  |
| `customer-service/src/main/java/com/awsbook/customer/ApplicationExceptionHandler.java` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 778) |  |
| `customer-service/src/main/java/com/awsbook/customer/MovieClient.java` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 796) |  |
| `customer-service/src/main/java/com/awsbook/customer/CustomerService.java` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 819) |  |
| `customer-service/src/main/java/com/awsbook/customer/CustomerController.java` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 846) |  |
| `customer-service/src/main/java/com/awsbook/customer/VersionController.java` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 878) |  |
| `customer-service/src/test/java/com/awsbook/customer/TestContainersConfiguration.java` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 900) |  |
| `customer-service/src/test/java/com/awsbook/customer/CustomerServiceApplicationTests.java` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 919) |  |
| `postgres/init.sql` | 19.1 › The sample application: two Spring Boot services › With the CLI (line 976) |  |
| `trust-eb.json` | 19.2 › The roles, the bundle, the application and its first version › With the CLI (line 93) |  |
| `trust-ec2.json` | 19.2 › The roles, the bundle, the application and its first version › With the CLI (line 99) |  |
| `parameter-read.json` | 19.2 › The roles, the bundle, the application and its first version › With the CLI (line 105) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `bundle/Procfile` | 19.3 › Immutable and traffic-splitting deployments on production › With the CLI (line 529) | rewritten later in the chapter |
| `bundle/.ebextensions/app.config` | 19.2 › The roles, the bundle, the application and its first version › With the CLI (line 160) |  |
| `stage-fragment.yaml` | 19.2 › The roles, the bundle, the application and its first version › With CloudFormation (line 241) |  |
| `dev-options.json` | 19.2 › The first environment: one instance and a coupled database › With the CLI (line 350) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `dev-fragment.yaml` | 19.2 › The first environment: one instance and a coupled database › With CloudFormation (line 529) |  |
| `greeting.config` | 19.2 › Configuration, properties and logs › With CloudFormation (line 686) |  |
| `deploy-fragment.yaml` | 19.2 › Deploying a version: the policies and an all-at-once deployment › With CloudFormation (line 818) |  |
| `client-fragment.yaml` | 19.3 › The database: coupled, decoupled and retained › With CloudFormation (line 171) |  |
| `prod-stack.yaml` | 19.3 › The production environment with CloudFormation › With CloudFormation (line 241) |  |
| `policy-fragment.yaml` | 19.3 › Immutable and traffic-splitting deployments on production › With CloudFormation (line 603) |  |
| `worker/Worker.java` | 19.4 › The worker tier: a queue, a daemon and a periodic task › With the CLI (line 208) |  |
| `worker/cron.yaml` | 19.4 › The worker tier: a queue, a daemon and a periodic task › With the CLI (line 232) |  |
| `worker/Procfile` | 19.4 › The worker tier: a queue, a daemon and a periodic task › With the CLI (line 239) |  |
| `worker-fragment.yaml` | 19.4 › The worker tier: a queue, a daemon and a periodic task › With CloudFormation (line 337) |  |
| `awsbook-ch19-ex-app/Procfile` | 19.4 › Try it yourself (line 561) |  |
| `awsbook-ch19-ex-cron.yaml` | 19.4 › Try it yourself (line 615) |  |
