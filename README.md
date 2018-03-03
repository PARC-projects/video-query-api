# Video Query API

## Dependencies

```bash
pip install Django==2.0.1
pip install djangorestframework==3.7.7
pip install django-cors-headers==2.1.0
pip install psycopg2==2.7.3.2
pip install pillow==5.0.0
pip install django-filter=1.1.0
```

## Database

- Create a database named "Video-Query"
- Run migration `python manage.py migrate`
- Create a super user `python manage.py createsuperuser`
- For all deployment, load fixture `python manage.py loaddata lookups`
- For dev, load fixture `python manage.py loaddata dev-init`
- For dev, load fixture `python manage.py loaddata dev-results`

## ENV Keys

- API_DEBUG
  - dev = False
- API_SECRET_KEY
  - dev = random number
- API_DB_NAME
- API_DB_USER
- API_DB_PASS
- API_DB_HOST
  - dev = localhost
- API_DB_PORT
  - dev = 5432
- ALLOWED_HOST
  - dev = Can be omitted
- API_CORS_ORIGIN_WHITELIST
  - dev = Can be omitted

For example, execute the following:
  - Mac: 
  ```bash
  source secrets.sh
  ```
  - Linux: 
  ```bash
  bash secrets.sh
  ```
