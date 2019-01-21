# Dependencies
FROM python:3.7-slim

# Setup working dir
WORKDIR /code
COPY /src /code

RUN pip install flask
RUN pip install pusher

RUN apt-get update
RUN apt-get install net-tools




CMD ["flask", "run"]
