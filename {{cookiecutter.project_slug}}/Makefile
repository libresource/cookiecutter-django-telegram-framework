test:
	python manage.py test

server:
	python manage.py runserver

prod_server:
	python manage.py runserver --settings={{cookiecutter.project_slug}}.prod_settings

coverage:
	coverage run --source='.' manage.py test
	coverage html
	coverage report --fail-under=100

yamllint:
	yamllint -d relaxed .

pylint:
	pylint $(shell git ls-files '*.py')

lint:
	make yamllint
	make pylint

run_bot:
	python manage.py run_bot --settings={{cookiecutter.project_slug}}.prod_settings
