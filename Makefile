SHELL := /bin/bash
AWS_ACCOUNT := 194086103172
AWS_REGION := eu-west-2

.PHONY: get-aws-credentials
get-aws-credentials:
	export AWS_PROFILE=people-data-system && \
	npx aws-azure-login --no-sandbox --mode gui

.PHONY: create-bootstrap-stack
create-bootstrap-stack:
	cdk bootstrap aws://${AWS_ACCOUNT}/${AWS_REGION}

.PHONY:	delete-bootstrap-stack
delete-bootstrap-stack:
	aws cloudformation delete-stack --stack-name CDKToolkit \
	--region ${AWS_REGION}

.PHONY: install-dev
install-dev:
	pip install -r requirements-dev.txt

.PHONY: install
install:
	pip install -r requirements.txt