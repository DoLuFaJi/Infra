FROM mongo

WORKDIR /code

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install kafka-python
RUN pip3 install pymongo

CMD ["/code/historisation.sh"]
#CMD ["python", "historisation.py"]
