init:
	python -m venv venv && \
	. venv/bin/activate && \
	pip install --no-cache-dir --upgrade -r requirements.txt
	pre-commit install
	npm install -g serverless
	sls plugin install -n serverless-python-requirements
	npm install serverless-offline --save-dev

set-deploy:
	npm install -g serverless
	sls plugin install -n serverless-python-requirements
	npm install serverless-offline --save-dev