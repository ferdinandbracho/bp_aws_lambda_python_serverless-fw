# AWS Lambda Python Boiler Plate

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/) [![Serverless Framework](https://img.shields.io/badge/serverless-3.0+-FD5750.svg)](https://www.serverless.com/) [![AWS Lambda Powertools](https://img.shields.io/badge/powertools-1.32-FF9900.svg)](https://awslabs.github.io/aws-lambda-powertools-python/latest/) [![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/ferdinandbracho/bp_aws_lambda_python_serverless-fw/deploy.yml?branch=main&logo=githubactions)](https://github.com/ferdinandbracho/bp_aws_lambda_python_serverless-fw/actions/workflows/deploy.yml?query=branch%3Amain)

This template repository serves as a starting point for developing [AWS Lambda](https://aws.amazon.com/lambda/) functions in [Python 3.12](https://www.python.org/downloads/release/python-3120/). It offers a well-structured boilerplate setup, complete with essential configurations, making it easier to kickstart your Lambda-based projects and streamline your serverless development process.

It includes a [pre-commit](https://pre-commit.com/) framework configured with [mypy](https://mypy.readthedocs.io/en/stable/index.html) and [ruff](https://beta.ruff.rs/docs/) to ensure consistent code formatting and strict typing. Dependencies are managed using [uv](https://github.com/astral-sh/uv) and defined in `pyproject.toml`.

Use this template as a starting point to quickly set up a robust and scalable AWS Python Lambda function.

## Table of Contents

- [Required](#required)
- [Features](#features)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Deployment](#deployment)
- [Offline](#offline)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

---

### Required

- Node 18 or higher
- Python 3.12
- [uv](https://github.com/astral-sh/uv) (Python package installer, can be installed via `pip install uv` or `curl -LsSf https://astral.sh/uv/install.sh | sh`)

## Features

- **Makefile to initialize the project:** The repository includes a Makefile that simplifies the project initialization process. By running the `make init` command, you can set up the project easily.
- **Pre-commit framework with MyPy and ruff:** The repository is configured with a pre-commit framework that enforces code formatting and strict typing checks using MyPy and ruff. This helps maintain code quality and adhere to best practices.
- **Initial serverless.yml configuration:** The repository includes an initial `serverless.yml` file that provides a basic configuration for deploying the Lambda function exposed through the AWS HTTP API Gateway.
- **GitHub Actions workflow integration:** The workflow can be customized. Currently, it is set to deploy the Lambda function when changes are pushed to the `main` branch.


## Usage

1. **Install `uv`:**
   If you don't have `uv` installed, you can install it via pip:
   ```sh
   pip install uv
   ```
   Or via curl (Linux/macOS):
   ```sh
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Init project:**

Position yourself in the project root directory and run the following command:

```sh
make init
```

This command will:
- Create a virtual environment named `.venv` using `uv`.
- Install all Python dependencies (including development dependencies like `ruff`, `mypy`, `pre-commit`) defined in `pyproject.toml` into the `.venv` using `uv`.
- Install pre-commit hooks.
- Install [Serverless framework](https://www.serverless.com/) globally using `npm`.
- Install the required Serverless plugins (`serverless-python-requirements`, `serverless-offline`).

3. **Activate the virtual environment:**
   After `make init` completes, activate the virtual environment:
   ```sh
   source .venv/bin/activate
   ```

### Makefile Commands

This project uses a `Makefile` to streamline common development tasks. Here are the available commands:

- **`make init`**: Initializes the project by setting up the virtual environment, installing dependencies (Python and Node.js for Serverless), and configuring pre-commit hooks. See detailed steps above.
- **`make lint`**: Runs linters (`ruff`) and type checkers (`mypy`) to ensure code quality and consistency. (Described further under 'Linting and Type Checking')
- **`make test`**: Executes the unit test suite using `pytest`. (Described further under 'Running Tests')
- **`make set-deploy`**: Installs/re-installs Serverless Framework globally and the `serverless-python-requirements` plugin. This can be useful for CI/CD environments or to ensure a consistent Serverless setup.

NOTE: The Serverless Framework assumes that you have the AWS CLI installed and configured.

## Environment Variables

**Local Development**

To set up environment variables for local development, follow these steps:

1. Create a `.env` file in the root directory of your project.
2. Add the necessary environment variables to the .env file in the format KEY=VALUE. Adjust the [config.py](config.py) file to insert these variables into the config class instance.

Example .env file:
```txt
DB_HOST=localhost
DB_PORT=5432
DB_USER=myuser
DB_PASSWORD=mypassword
```

**Deployed**

For deployment, you'll need to set up environment variables or secrets in your GitHub repository. Here's how to do it:

1. Create the required environment variables or secrets in your GitHub repository.
2. In the [github-actions workflow file](.github/workflows/deploy.yaml), locate the "Deploy AWS Lambda" step.
3. Insert the environment variables or secrets into the workflow step, providing the necessary values.

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

4. Then add the env variables in [serverless.yml](serverless.yml) to let serverless framework know about the env variables to insert in the lambda. This in "Provider" section using "environment" attribute:

Example insertion:

```yml
provider:
  name: aws
  runtime: python3.12
  environment:
    SERVICE_TRX_TRIPS: ${env:DB_HOST}
    SERVICE_TRX_CLIENTS: ${env:DB_PORT}
    SERVICE_TRX_ROUTES: ${env:DB_USER}
```

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

NOTE: In current form, after deployment, your API is public and can be invoked by anyone. For production deployments, you might want to configure an authorizer. For details on how to do that, refer to [serverless httpApi event docs](https://www.serverless.com/framework/docs/providers/aws/events/http-api#lambda-request-authorizers).

After deploying, you will have the following components:

- An S3 bucket associated with the code of your Lambda function.
- A Lambda function in the AWS Lambda service.
- An HTTP API Gateway integrated with the Lambda function. This API Gateway acts as a front-facing interface for invoking your Lambda function over HTTP.


## Offline

To run your Lambda functions locally for testing purposes, you can use the sls command with the `offline` option. This will start a local development server that simulates the AWS environment.

To run the serverless offline:

```sh
sls offline
```

## Linting and Type Checking

To lint the code with Ruff and type check with MyPy:

```bash
make lint
```

### Running Tests

This project uses `pytest` for unit testing. Tests are located in the `tests/` directory.

To run the tests:

```bash
make test
```

This command will execute `pytest` using `uv run` and display the test results, including code coverage information as configured in `pytest.ini`.

## Documentation

Please ensure you update this README after implementing an instance of this template. Here are the recommended steps to follow:

### 1. Introduction and Overview

In your README's "Introduction and/or Overview" section (or similar), include the following information:

```markdown
The Lambda function is built using Python 3.12 and is based on the [Core Lambda Template](https://github.com/ferdinandbracho/bp_aws_lambda_python_serverless-fw). For comprehensive technical details, instructions on how to run, deploy, and any other related considerations, please refer to the documentation provided in the [template repository](https://github.com/ferdinandbracho/bp_aws_lambda_python_serverless-fw).
```
### 2 Installation and Prerequisites

Towards the end of your README, just before the "Contributing" section (if applicable), add links to specific sections of the template repository for installation and prerequisites information:
```markdown
  ## Installation and Prerequisites

  - [**Requisites**](https://github.com/ferdinandbracho/bp_aws_lambda_python_serverless-fw#required)
  - [**Usage**](https://github.com/Traxi-on/core_template_aws_lambda_python#usage)
  - [**Deployment**](https://github.com/Traxi-on/core_template_aws_lambda_python#deployment)
```

By following these steps, you'll ensure that users can easily find comprehensive information about your service and how it relates to the template.

## **Contributing**

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Implement your changes.
4. Write or update tests as necessary.
5. Submit a pull request against the main branch.

Please ensure your code adheres to the project's coding standards and includes appropriate tests.