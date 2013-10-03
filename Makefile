setup:
	@pip install -r requirements.txt

run:
	@python quiz/manage.py runserver 0.0.0.0:8000

syncdb:
	@python quiz/manage.py syncdb