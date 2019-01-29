FROM mongo

WORKDIR /code

RUN apt-get update
RUN apt-get install -y python3 python-pip
RUN pip install --upgrade pip
RUN pip install kafka-python
RUN pip install pymongo

CMD ["python", "historisation.py"]
