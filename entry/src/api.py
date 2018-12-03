from flask import (
    Flask,
    render_template,
    jsonify,
    request
)

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
    print('wesh recu')
    return jsonify(request.json.data)

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
