.PHONY: help init test build-lambda
.DEFAULT_GOAL=help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

create: build  ## create env
	@sceptre launch-env serverless

delete: ## delete env
	@sceptre delete-env serverless

deploy: delete create info ## delete and create

info: ## describe resources
	@sceptre describe-stack-outputs serverless api

build: ## package the lambdas
	./build.sh

init: ## initializes a python environment
	pipenv install --three --dev

rm: ## removes a python environment
	pipenv --rm

test: ## run unit tests
	pipenv run pytest -s -v tests

