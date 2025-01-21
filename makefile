run:
	python3 manage.py runserver

migrate:
	python3 manage.py migrate

migrations:
	python3 manage.py make_migrations

install:
	python3 -m pip install -r requirements.txt

compile_requirements:
	python3 -m pip-compile requirements.in