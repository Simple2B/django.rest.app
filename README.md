# Creating environment

```
git init
git clone https://github.com/Simple2B/django.rest.app.git
cd django.rest.app
poetry install
cp sample.env .env
```

# Launch and run application locally

```
source .venv/bin/activate
python manage.py migrate
python manage.py runserver
```

# Run docker

```
docker compose up app
```
