FROM ubuntu:latest

RUN apt-get update && apt-get install -y wget 

RUN apt-get install -y python3 \
    python3-pip 

RUN pip3 install flask \
	mysql-connector-python==8.0.19

WORKDIR /app

COPY app.py db.py cert.pem cleardb-ca.pem unlock-key.pem /app/

ENV FLASK_APP /app/app.py

CMD flask run -h 0.0.0.0 -p $PORT
