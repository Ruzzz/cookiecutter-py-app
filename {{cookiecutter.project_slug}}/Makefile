run:
	{{cookiecutter.const_prefix}}_CONF=dev python -m {{cookiecutter.project_slug}}.app

check:
	pylint {{cookiecutter.project_slug}} && mypy {{cookiecutter.project_slug}}

test:
	pytest --disable-pytest-warnings --cov={{cookiecutter.project_slug}} {{cookiecutter.project_slug}}/tests

-include Makefile.local
