## Makefile for Init-Projects ##

init:
	@poetry install
	@poetry shell
	@poetry run pre-commit install

pre-commit:
	@git add .
	@poetry run pre-commit run

commit:
	@cz commit
