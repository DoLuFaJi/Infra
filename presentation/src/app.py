import json
import requests
import threading
from flask import Flask, render_template, request
from pusher import Pusher
from kafka import KafkaProducer, KafkaConsumer

from settings import ENTRYPOINT, MY_TOPIC


class Consume(threading.Thread):
	def __init__(self, my_topic):
		threading.Thread.__init__(self)
		self.topic = my_topic
		self._stop_event = threading.Event()

	def run(self):
		consumer_in = KafkaConsumer(self.topic, bootstrap_servers='reception:9092', auto_offset_reset='smallest')
		for msg in consumer_in:
			res = requests.post(ENTRYPOINT, data=msg.value.decode('utf-8'))

	def stop(self):
		self._stop_event.set()

	def stopped(self):
		self._stop_event.is_set()


consume = Consume(MY_TOPIC)
app = Flask(__name__)
pusher = Pusher(app_id=u'695721', key=u'ca74e69b1d763f09e09b', secret=u'ad6425c1e00b57d69dee', cluster=u'eu')


@app.route('/')
def dashboard():
	"""
	This function just responds to the browser ULR
	localhost:8080/"""
	return render_template('dashboard.html')


@app.route('/consume', methods=['POST'])
def demo():
	consume.start()
	return render_template('dashboard.html')


@app.route('/message', methods=['POST'])
def message():
	data = json.loads(request.data.decode('utf-8'))
	pusher.trigger(u'message', u'send', {
		u'name': str(data['cashReceiptID']),
		u'message': str(data['customerID'])
	})
	return render_template('dashboard.html')


@app.route('/kill')
def stop_to_consume():
	consume.stop()
	consume.join()
	return render_template('dashboard.html')


""" TO DELETE SOON
@app.route('/orders', methods=['POST'])
def order():
	data = request.form
	pusher.trigger(u'order', u'place', {
		u'units': data['units']
	})
	return "units logged"

@app.route('/customer', methods=['POST'])
def customer():
	data = request.form
	pusher.trigger(u'customer', u'add', {
		u'name': data['name'],
		u'position': data['position'],
		u'office': data['office'],
		u'age': data['age'],
		u'salary': data['salary'],
	})
	return "customer added"
"""

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
