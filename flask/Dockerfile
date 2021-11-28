FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 \
    python3-pip \
    build-essential \
    python3-dev \
    libmysqlclient-dev

RUN pip3 install flask \
	mysql-connector-python==8.0.19 \
	sqlalchemy \
	numpy \
	pandas \
	bokeh==2.2.0 \
	mysqlclient

WORKDIR /app

COPY . /app/

ENV FLASK_APP /app/app.py

CMD flask run -h 0.0.0.0 -p $PORT
