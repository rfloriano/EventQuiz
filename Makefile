setup:
	@pip install -r requirements.txt

run:
	@python manage.py runserver 0.0.0.0:8000

shell:
	@python manage.py shell

syncdb:
	@python manage.py syncdb