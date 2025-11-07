# carl_and_andrew_django_w_help_from_joe

https://github.com/docker/awesome-compose/tree/master/official-documentation-samples/django/

from scratch

`sudo docker compose run web django-admin startproject evezor_app .`

change settings.py 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}
```
`docker compose up --build`

`python manage.py migrate`
`python manage.py createsuperuser`


tutorial https://www.youtube.com/watch?v=rHux0gMZ3Eg

`python manage.py startapp playground`

### /Setup


`docker compose up --build`

`python manage.py migrate`

`python manage.py createsuperuser`

