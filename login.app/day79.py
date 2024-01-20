from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    # Do something with the data, for now, just return it as JSON
    return jsonify({'username': username, 'email': email, 'password': password})

# Main execution point
if __name__ == '__main__':
    # Run the Flask app on host '0.0.0.0' and port 8081 in debug mode
    app.run(host='0.0.0.0', port=8081, debug=True)
