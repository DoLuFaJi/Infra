import ast
import json
import requests
import threading
from flask import Flask, render_template, request
from pusher import Pusher
from kafka import KafkaProducer, KafkaConsumer

from settings import ENTRYPOINT, MY_TOPIC


app = Flask(__name__)
pusher = Pusher(app_id=u'703310', key=u'4adcbc6f4cdd9aed0a57', secret=u'83853fb9750d891163bb', cluster=u'eu')
verrou = threading.RLock()


class Consume(threading.Thread):
	def __init__(self, my_topic):
		threading.Thread.__init__(self)
		self.topic = my_topic
		self._is_running = True

	def run(self):
		self.consumer_in = KafkaConsumer(self.topic, bootstrap_servers='reception:9092', auto_offset_reset='smallest')
		for msg in self.consumer_in:
			with verrou:
				if not self._is_running:
					return None
				res = requests.post(ENTRYPOINT, data=msg.value.decode('utf-8'))

	def stop(self):
		self.consumer_in.close()
		self._is_running = False

	def stopped(self):
		pass



@app.route('/')
def dashboard():
	"""
	This function just responds to the browser ULR
	localhost:8080/"""
	return render_template('dashboard.html')


@app.route('/consume', methods=['POST'])
def demo():
	global consume
	consume = Consume(MY_TOPIC)
	consume.start()
	return render_template('dashboard.html')


@app.route('/message', methods=['POST'])
def message():
	data = ast.literal_eval(request.data.decode('utf-8'))
	pusher.trigger(u'customer', u'add', {
		u'store_id': data[0],
		u'type_payment': data[1],
		u'nb_transactions': data[2],
	})
	return render_template('dashboard.html')


@app.route('/stop', methods=['POST'])
def stop_to_consume():
	with verrou:
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
