from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dictionary to store valid username-email-password combinations
valid_users = {
    'Karlie': {'email': 'karliemoyo@gmail.com', 'password': '078525'},
    'Abraham ': {'email': 'abrahamola@gmail.com', 'password': 'yes'},
    'Clara': {'email': 'claramorris@gmail.com', 'password': 'hello'},
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user_data = valid_users[username]
        if user_data['email'] == email and user_data['password'] == password:
            return jsonify({'valid': True})
        else:
            return jsonify({'valid': False})
    except KeyError:
        return jsonify({'valid': False})

@app.route('/welcome')
def welcome():
    return 'Welcome! Take a seat.'

@app.route('/naughty')
def naughty():
    return 'Naughty step hacker! This is the page for non-valid users.'

if __name__ == '__main__':
    app.run(debug=True)
