from flask import Flask, render_template, request
from pusher import Pusher

app = Flask(__name__)
pusher = Pusher(app_id=u'695721', key=u'ca74e69b1d763f09e09b', secret=u'ad6425c1e00b57d69dee', cluster=u'eu')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/dashboard')
def dashboard():
	"""
	This function just responds to the browser ULR
	localhost:5000/"""
	return render_template('dashboard.html')

@app.route('/orders', methods=['POST'])
def order():
	data = request.form
	pusher.trigger(u'order', u'place', {
		u'units': data['units']
	})
	return "units logged"

@app.route('/message', methods=['POST'])
def message():
	data = request.form
	pusher.trigger(u'message', u'send', {
		u'name': data['name'],
		u'message': data['message']
	})
	return "message sent"

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

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
