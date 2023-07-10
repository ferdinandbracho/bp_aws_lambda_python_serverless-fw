# AWS Lambda Python Boiler Plate
This template repository provides a boilerplate setup for building an AWS Lambda function using Python 3.9. The [Serverless Framework](https://www.serverless.com/) is used to create the necessary infrastructure.

The repository includes a pre-commit framework configured with MyPy and ruff to ensure consistent code formatting and strict typing. This helps maintain code quality and adherence to best practices.

Use this template as a starting point to quickly set up a robust and scalable AWS Python Lambda function.

### Required
- Node 18 or higher
- Python 3.9

## Features
- Makefile to initialize the project: The repository includes a Makefile that simplifies the project initialization process. By running the make init command
- Pre-commit framework with MyPy and ruff: The repository is configured with a pre-commit framework that enforces code formatting and strict typing checks using MyPy and ruff.
- Initial serverless.yml configuration: The repository includes an initial serverless.yml file that provides a basic configuration for deploying the Lambda function exposed through the AWS HTTP API Gateway.
- GitHub [Actions workflow](.github/workflows/deploy.yaml) integration: The workflow can be customized. Currently is set to deploying the Lambda function when push changes on main.

## Usage
- Init project:
    - create and activate a [virtual env](https://docs.python.org/3/library/venv.html#module-venv)
    - install initial dependencies
    - install pre-commit configuration
    - install [serverless framework](https://www.serverless.com/)
    - Install the required Serverless plugins:
        - [Serverless offile](https://www.serverless.com/plugins/serverless-offline): To test and run locally.
        - [Python requirements](https://www.serverless.com/plugins/serverless-python-requirements): To handle third-party dependencies.

Position yourself in the project root directory and run the following command:
```sh
    make init
```

_*NOTE: The Serverless Framework assumes that you have the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) installed and configured*_

The initial [serverless.yml](serverless.yml) use the default AWS CLI profile related to an IAM user with sufficient privileges to interact with Lambda and S3 services. Adjust this profile according to your needs.

## Environment Variables
**Local Development**
- Create a .env file in the root directory of your project.
- Add the necessary environment variables to the .env file in the format KEY=VALUE. Adjust the [config.py](config.py) file to insert these variables into the config class instance.
Example .env file:
```txt
DB_HOST=localhost
DB_PORT=5432
DB_USER=myuser
DB_PASSWORD=mypassword
```

**Deployed**
- Create the required environment variables or secrets in GitHub repository
- In the [github-actions workflow file](.github/workflows/deploy.yaml), locate the "Deploy AWS Lambda" step.
- Insert the environment variables or secrets into the workflow step, providing the necessary values.
Example workflow step:
```yaml
- name: Deploy AWS Lambda
  env:
    DB_HOST: ${{ secrets.DB_HOST }}
    DB_PORT: ${{ secrets.DB_PORT }}
    DB_USER: ${{ secrets.DB_USER }}
    DB_PASSWORD: ${{ secrets.DB_PASSWORD }}
  run: |
    # Add your deployment script here
```
Create github-actions secrets/variables and insert in  in the "Deploy AWS Lambda" step
## Deployment
To interact with deployment, removal, and redeployment, use the [serverless CLI ](https://www.serverless.com/framework/docs/providers/aws/cli-reference)

Basic commands:
- Deploy
```sh
serverless deploy
```
- Remove
```sh
serverless remove
```

_NOTE: In current form, after deployment, your API is public and can be invoked by anyone. For production deployments, you might want to configure an authorizer. For details on how to do that, refer to [serverless httpApi event docs](https://www.serverless.com/framework/docs/providers/aws/events/http-api#lambda-request-authorizers)._

After deploying, you will have the following components:

- An S3 bucket associated with the code of your Lambda function.

- A Lambda function in the AWS Lambda service.

- An HTTP API Gateway integrated with the Lambda function. This API Gateway acts as a front-facing interface for invoking your Lambda function over HTTP.

## **Contributing**
Contributions are welcome!
Please submit pull requests or open issues for any improvements or bug fixes.