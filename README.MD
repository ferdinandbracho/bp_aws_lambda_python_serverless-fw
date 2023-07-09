# AWS Lambda Python Boiler Plate
This template repository provides a boilerplate setup for building a aws lambda running in python 3.9. For this we use [serverless framework](https://www.serverless.com/)to create the needed infrastructure

The repository includes a pre-commit framework configured with MyPy and ruff to ensure consistent code formatting and strict typing. This helps maintain code quality and adherence to best practices.

Use this template as a starting point to quickly set up a robust and scalable aws python lambda.

### Required
- Node 18>
- Python 3.9

## Features
-
- Pre-commit framework with MyPy and ruff for code formatting and strict typing checks

## Usage
- Init project:
    - create and activate a [virtual env](https://docs.python.org/3/library/venv.html#module-venv)
    - install initial dependencies
    - install pre-commit config
    - install [serverless framework](https://www.serverless.com/)
    - Install serverless needed plugins
        - [Serverless offile](https://www.serverless.com/plugins/serverless-offline) - To test and run locally
        - [Python requirements](https://www.serverless.com/plugins/serverless-python-requirements) - To handled third party dependencies.

Positioning in the project root, run the following make command:
```sh
    make init
```

_*NOTE: Serverless assume that you have [aws cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) install and configure*_

The initial [serverless.yml](serverless.yml) spec an aws cli profile called "trxbiz-deploy" related to a IAM user with sufficient privileges interact with lambda and s3 services. Adjust this profile to your needs


## Deployment
Use [serverless CLI ](https://www.serverless.com/framework/docs/providers/aws/cli-reference) to intereact with deploy, remove and redeploy

Basic command:
- Deploy
```sh
serverless deploy
```
- Remove
```sh
serverless remove
```

_NOTE: In current form, after deployment, your API is public and can be invoked by anyone. For production deployments, you might want to configure an authorizer. For details on how to do that, refer to [serverless httpApi event docs](https://www.serverless.com/framework/docs/providers/aws/events/http-api#lambda-request-authorizers)._


## **Contributing**
Contributions are welcome!
Please submit pull requests or open issues for any improvements or bug fixes.