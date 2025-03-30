FROM python:3.10.12

RUN apt-get update

WORKDIR /open_courses
COPY . /open_courses/1

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1
EXPOSE 8000