from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads
import json
import threading

#class Consumer(threading.Thread):
class Comsumer():
    daemon = True

    msg = {
        "cashReceiptID": "2",
        "storeID": "2",
        "terminalID": "2",
        "agentID": "2",
        "customerID": "2",
        "date": "2017-11-18 20:39:32",
        "lines": [
            {
                "unitOfMeasure": "measure",
                "settlementAmount": 0.68,
                "creditAmount": 0.62,
                "lineNumber": 1,
                "unitPrice": 0.31,
                "productCode": "00000010",
                "taxPercentage": 10,
                "productDescription": "---",
                "productCategoryName": "Kertel",
                "productCategoryCode": "3",
                "quantity": 2
            }
        ]
    }

    consumer = KafkaConsumer(
        'msg_in',
        bootstrap_servers=['reception:9092'],
        auto_offset_reset='smallest',
        enable_auto_commit=True,
        auto_commit_interval_ms=100,
        # group_id='group',
        #value_deserializer=lambda v: json.dumps(v).encode('utf-8')
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )

    # consumer = KafkaConsumer('foobar', bootstrap_servers='reception:9092', auto_offset_reset='smallest')

    client = MongoClient('mongodb://Infra:Infra@localhost:27017/historisation')
    db = client['historisation']
    db.authenticate('Infra','Infra')
    collection = db['cashreceipt']
    #print(client.list_database_names())

    for message in consumer:
        message = message.value
        print(message)
        collection.insert_one(message)




'''
    while True:
        msg = consumer.poll()
        collection.insert_one(msg)
        print('{} added to {}'.format(message, collection))
'''



Comsumer()
