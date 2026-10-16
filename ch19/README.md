# 19 - Elastic Beanstalk and the Spring Boot sample application

The files the chapter **19 - Elastic Beanstalk and the Spring Boot sample application** of the AWS tutorial writes in its command blocks, copied byte for byte from the chapter. The blocks write them into the work folder `~/awsbook-ch19`; cloning this folder there gives the same files. The chapter explains every line; the table says where each file is written: the section heading and the line where the file's text starts.

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
| `movie-service/pom.xml` | The sample application: two Spring Boot services › With the CLI (line 269) |  |
| `movie-service/Dockerfile` | The sample application: two Spring Boot services › With the CLI (line 342) |  |
| `movie-service/src/main/resources/application.properties` | The sample application: two Spring Boot services › With the CLI (line 349) |  |
| `movie-service/src/main/resources/schema.sql` | The sample application: two Spring Boot services › With the CLI (line 356) |  |
| `movie-service/src/main/resources/data.sql` | The sample application: two Spring Boot services › With the CLI (line 364) |  |
| `movie-service/src/main/java/com/awsbook/movie/MovieServiceApplication.java` | The sample application: two Spring Boot services › With the CLI (line 382) |  |
| `movie-service/src/main/java/com/awsbook/movie/Genre.java` | The sample application: two Spring Boot services › With the CLI (line 395) |  |
| `movie-service/src/main/java/com/awsbook/movie/MovieDto.java` | The sample application: two Spring Boot services › With the CLI (line 400) |  |
| `movie-service/src/main/java/com/awsbook/movie/Movie.java` | The sample application: two Spring Boot services › With the CLI (line 405) |  |
| `movie-service/src/main/java/com/awsbook/movie/MovieRepository.java` | The sample application: two Spring Boot services › With the CLI (line 427) |  |
| `movie-service/src/main/java/com/awsbook/movie/MovieController.java` | The sample application: two Spring Boot services › With the CLI (line 437) |  |
| `movie-service/src/main/java/com/awsbook/movie/VersionController.java` | The sample application: two Spring Boot services › With the CLI (line 466) |  |
| `movie-service/src/test/java/com/awsbook/movie/TestContainersConfiguration.java` | The sample application: two Spring Boot services › With the CLI (line 489) |  |
| `movie-service/src/test/java/com/awsbook/movie/MovieServiceApplicationTests.java` | The sample application: two Spring Boot services › With the CLI (line 508) |  |
| `customer-service/pom.xml` | The sample application: two Spring Boot services › With the CLI (line 563) |  |
| `customer-service/Dockerfile` | The sample application: two Spring Boot services › With the CLI (line 640) |  |
| `customer-service/src/main/resources/application.properties` | The sample application: two Spring Boot services › With the CLI (line 647) |  |
| `customer-service/src/main/resources/schema.sql` | The sample application: two Spring Boot services › With the CLI (line 655) |  |
| `customer-service/src/main/resources/data.sql` | The sample application: two Spring Boot services › With the CLI (line 662) |  |
| `customer-service/src/main/java/com/awsbook/customer/CustomerServiceApplication.java` | The sample application: two Spring Boot services › With the CLI (line 673) |  |
| `customer-service/src/main/java/com/awsbook/customer/Genre.java` | The sample application: two Spring Boot services › With the CLI (line 686) |  |
| `customer-service/src/main/java/com/awsbook/customer/MovieDto.java` | The sample application: two Spring Boot services › With the CLI (line 691) |  |
| `customer-service/src/main/java/com/awsbook/customer/CustomerDto.java` | The sample application: two Spring Boot services › With the CLI (line 696) |  |
| `customer-service/src/main/java/com/awsbook/customer/GenreUpdateRequest.java` | The sample application: two Spring Boot services › With the CLI (line 703) |  |
| `customer-service/src/main/java/com/awsbook/customer/Customer.java` | The sample application: two Spring Boot services › With the CLI (line 708) |  |
| `customer-service/src/main/java/com/awsbook/customer/CustomerRepository.java` | The sample application: two Spring Boot services › With the CLI (line 738) |  |
| `customer-service/src/main/java/com/awsbook/customer/CustomerNotFoundException.java` | The sample application: two Spring Boot services › With the CLI (line 745) |  |
| `customer-service/src/main/java/com/awsbook/customer/ApplicationExceptionHandler.java` | The sample application: two Spring Boot services › With the CLI (line 754) |  |
| `customer-service/src/main/java/com/awsbook/customer/MovieClient.java` | The sample application: two Spring Boot services › With the CLI (line 772) |  |
| `customer-service/src/main/java/com/awsbook/customer/CustomerService.java` | The sample application: two Spring Boot services › With the CLI (line 795) |  |
| `customer-service/src/main/java/com/awsbook/customer/CustomerController.java` | The sample application: two Spring Boot services › With the CLI (line 822) |  |
| `customer-service/src/main/java/com/awsbook/customer/VersionController.java` | The sample application: two Spring Boot services › With the CLI (line 854) |  |
| `customer-service/src/test/java/com/awsbook/customer/TestContainersConfiguration.java` | The sample application: two Spring Boot services › With the CLI (line 877) |  |
| `customer-service/src/test/java/com/awsbook/customer/CustomerServiceApplicationTests.java` | The sample application: two Spring Boot services › With the CLI (line 896) |  |
| `postgres/init.sql` | The sample application: two Spring Boot services › With the CLI (line 953) |  |
| `trust-eb.json` | The roles, the bundle, the application and its first version › With the CLI (line 1141) |  |
| `trust-ec2.json` | The roles, the bundle, the application and its first version › With the CLI (line 1147) |  |
| `parameter-read.json` | The roles, the bundle, the application and its first version › With the CLI (line 1153) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `bundle/Procfile` | Immutable and traffic-splitting deployments on production › With the CLI (line 2335) | rewritten later in the chapter |
| `bundle/.ebextensions/app.config` | The roles, the bundle, the application and its first version › With the CLI (line 1209) |  |
| `stage-fragment.yaml` | The roles, the bundle, the application and its first version › With CloudFormation (line 1298) |  |
| `dev-options.json` | The first environment: one instance and a coupled database › With the CLI (line 1389) | a template: the shell fills in $VARIABLES when the chapter runs it |
| `dev-fragment.yaml` | The first environment: one instance and a coupled database › With CloudFormation (line 1575) |  |
| `greeting.config` | Configuration, properties and logs › With CloudFormation (line 1726) |  |
| `deploy-fragment.yaml` | Deploying a version: the policies and an all-at-once deployment › With CloudFormation (line 1850) |  |
| `client-fragment.yaml` | The database: coupled, decoupled and retained › With CloudFormation (line 1988) |  |
| `prod-stack.yaml` | The production environment with CloudFormation › With CloudFormation (line 2047) |  |
| `policy-fragment.yaml` | Immutable and traffic-splitting deployments on production › With CloudFormation (line 2415) |  |
| `worker/Worker.java` | The worker tier: a queue, a daemon and a periodic task › With the CLI (line 2572) |  |
| `worker/cron.yaml` | The worker tier: a queue, a daemon and a periodic task › With the CLI (line 2596) |  |
| `worker/Procfile` | The worker tier: a queue, a daemon and a periodic task › With the CLI (line 2603) |  |
| `worker-fragment.yaml` | The worker tier: a queue, a daemon and a periodic task › With CloudFormation (line 2707) |  |
| `awsbook-ch19-ex-app/Procfile` | Try it yourself (line 2937) |  |
| `awsbook-ch19-ex-cron.yaml` | Try it yourself (line 2991) |  |
