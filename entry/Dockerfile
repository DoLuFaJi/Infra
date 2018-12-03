# Dependencies
FROM python:3.7-slim

# Setup working dir
WORKDIR /app
COPY /src /app

RUN pip install flask

CMD ["python", "generator.py"]
