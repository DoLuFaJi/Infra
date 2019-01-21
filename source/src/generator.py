import requests
import random
import time
from threading import Thread
import json

from cashReceipt import generateCashReceipt, writeJSON
from settings import ENTRYPOINT, STORE_ID, TERMINAL_ID, AGENT_ID, CUSTOMER_ID, WAIT_TIME

class Store(Thread):
    def __init__(self, storeId):
        Thread.__init__(self)
        self.storeId = storeId
        self.nbReceipts = 0
        self.power = len(str(STORE_ID[1]))

    def __generate_id_linked_store_id__(self, min_id, max_id):
        return random.randint(min_id, max_id)*(10**self.power)+self.storeId

    def __generate_receipt_id__(self):
        self.nbReceipts += 1
        return self.nbReceipts*(10**self.power)+self.storeId

    def run(self):
        while True:
            receiptId = self.__generate_receipt_id__()
            terminalId = self.__generate_id_linked_store_id__(TERMINAL_ID[0], TERMINAL_ID[1])
            agentId = self.__generate_id_linked_store_id__(AGENT_ID[0], AGENT_ID[1])
            customerId = random.randint(CUSTOMER_ID[0], CUSTOMER_ID[1])
            time.sleep(WAIT_TIME)
            cashRec = generateCashReceipt(str(receiptId), str(self.storeId), str(terminalId), str(agentId), str(customerId))
            cashRec_json = json.dumps(cashRec)
            print("receiptid"+str(receiptId)+"storeid"+str(self.storeId)+"terminalid"+str(terminalId)+"agentid"+str(agentId)+"customerid"+str(customerId))
            res = requests.post(ENTRYPOINT, data=cashRec_json)
            print(res)


if __name__ == "__main__":
    current_store_id = STORE_ID[0]
    stores = []
    while current_store_id <= STORE_ID[1]:
        current_store = Store(current_store_id)
        current_store.start()
        stores.append(current_store)
        current_store_id += 1

    for store in stores:
        store.join()

