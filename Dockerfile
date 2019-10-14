# pull official base image
FROM python:3.7.4-alpine

# set work directory
RUN mkdir /code
WORKDIR /code

# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

# Needed for pillow
RUN apk add jpeg-dev zlib-dev

# Needed for pyscopg
RUN apk add postgresql-dev gcc python3-dev musl-dev

COPY ./requirements.txt /code/
RUN pip install -r requirements.txt

# copy project
COPY ./src/ /code/

# run entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]
