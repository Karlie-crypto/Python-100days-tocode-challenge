from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# For simplicity, using a dictionary as an in-memory database.
# In a real-world scenario, you should use a proper database.
users_db = {}


@app.route('/')
def index():
    return 'Welcome to the Flask Signup/Login App!'


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']

        # Check if the username already exists
        if username in users_db:
            return 'Username already exists. Please choose another username.'

        # Store user details in the database
        users_db[username] = {'name': name, 'password': password}

        return redirect(url_for('login'))

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username exists and the password is correct
        if username in users_db and users_db[username]['password'] == password:
            return f'Hello, {users_db[username]["name"]}!'

        return 'Invalid username or password. Please try again.'

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)

