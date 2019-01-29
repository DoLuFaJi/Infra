import requests
import random
import time
import json

from cashReceipt import generateCashReceipt, writeJSON
from settings import ENTRYPOINT, RECEIPT_ID, STORE_ID, TERMINAL_ID, AGENT_ID, CUSTOMER_ID, WAIT_TIME


# TODO add list of agents, store, list of terminals in settings
# 1 generator per store in future
while True:
	storeId = random.randint(STORE_ID[0], STORE_ID[1])
	receiptId = random.randint(RECEIPT_ID[0], RECEIPT_ID[1])
	terminalId = random.randint(TERMINAL_ID[0], TERMINAL_ID[1])
	agentId = random.randint(AGENT_ID[0], AGENT_ID[1])
	customerId = random.randint(CUSTOMER_ID[0], CUSTOMER_ID[1])
	time.sleep(random.random())
	cashRec = generateCashReceipt(str(receiptId), str(storeId), str(terminalId), str(agentId), str(customerId))
	cashRec_json = json.dumps(cashRec)
	res = requests.post(ENTRYPOINT, data=cashRec_json)
