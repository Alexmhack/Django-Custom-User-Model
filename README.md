# Django-Custom-User-Model
Customizing authentication in Django by creating a custom user model

1. Create virtualenv
	```
	pipenv install django 	<- install django using pipenv
	pipenv shell	<- activate virtualenv
	```

2. Start Django project
	```
	django-admin startproject custom
	python manage.py startapp accounts
	```
	Add ```'accounts'``` in **settings.py** ```INSTALLED_APPS```

3. Creating custom model in **accounts/models.py** and registering the model in **accounts/admins.py**. Checkout the code from the repo.

4. Running the ```makemigrations``` and ```migrate``` commands
	```
	python manage.py makemigrations
	python manage.py migrate
	```

5. Creating super user
	```
	python manage.py createsuperuser
	```
