FROM python:3

RUN mkdir -p /app
WORKDIR /app

ADD requirements.txt /app
ADD myapp.py /app
RUN pip3 install -r requirements.txt

EXPOSE 8000

