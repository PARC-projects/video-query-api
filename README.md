# Video Query API

## Dependencies

```bash
pip install Django==2.0.1
pip install djangorestframework==3.7.7
pip install django-cors-headers==2.1.0
pip install psycopg2==2.7.3.2
pip install pillow==5.0.0
```

## Database

- Create a database named "Video-Query"
- Run migration `python manage.py migrate`
- Create a super user `python manage.py createsuperuser`
- For dev, load fixture `python manage.py loaddata dev-init`
- For dev, load fixture `python manage.py loaddata dev-results`

## ENV Keys
- os.environ['API_DEBUG']
- os.environ['API_SECRET_KEY']
- os.environ['API_DB_NAME']
- os.environ['API_DB_USER']
- os.environ['API_DB_PASS']
- os.environ['API_DB_HOST']
- os.environ['API_DB_PORT']
- os.environ['ALLOWED_HOST']
