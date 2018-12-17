from flask import (
    Flask,
    render_template,
    jsonify,
    request
)
import json
import datetime
from time import time
from kafka import KafkaProducer

PRODUCE_KAFKA = True

def fromTimeStampToDate(timestamp):
	return datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

# Create the application instance
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')


@app.route('/api/ticket', methods=['POST'])
def add_ticket():
    json_obj = json.loads(request.data.decode('utf-8'))
    json_obj['entry_time'] = fromTimeStampToDate(time())
    if PRODUCE_KAFKA:
        producer = KafkaProducer(bootstrap_servers='reception:9092')
        producer.send('msg_in', json.dumps(json_obj))
    return jsonify({'status':'sucess'})

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
