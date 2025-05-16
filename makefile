SHELL := /bin/bash

.PHONY: init clean lint test deploy package offline logs

init:
	@echo "Initializing project dependencies and virtual environment with uv..."
	@if [ ! -d ".venv" ]; then \
		python3.12 -m venv .venv; \
	fi
	@source .venv/bin/activate; \
	uv pip sync pyproject.toml --all-extras; \
	pre-commit install; \
	@echo "Installing Serverless Framework and plugins globally and locally..."
	npm install -g serverless
	sls plugin install -n serverless-python-requirements
	npm install serverless-offline --save-dev

lint:
	@echo "Linting with Ruff..."
	@uv run ruff check .
	@echo "Type checking with MyPy..."
	@uv run mypy .

test:
	@echo "Running tests with pytest..."
	@uv run pytest

set-deploy:
	npm install -g serverless
	sls plugin install -n serverless-python-requirements
	npm install serverless-offline --save-dev