# Dependencies
FROM python:3.7-slim

# Setup working dir
WORKDIR /code
COPY /src /code

RUN pip install flask
RUN pip install kafka-python
RUN pip install pusher
RUN pip install requests

EXPOSE 5000
ENV FLASK_APP app.py

ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]
