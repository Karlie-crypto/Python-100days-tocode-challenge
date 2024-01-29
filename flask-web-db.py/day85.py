from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "078525"  # Change this to a secure secret key

# Sample valid usernames
valid_usernames = {'Karlie', 'Eric', 'Ben'}  # Add your valid usernames here

@app.route('/')
def index():
    if 'loggedIn' not in session or not session['loggedIn']:
        return redirect('/login')
    return render_template('index.html', username=session['username'])


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        # Check if user is already logged in
        if 'loggedIn' in session and session['loggedIn']:
            return render_template('login.html', message='User already logged in.')

        # Check if the entered username is valid
        if username in valid_usernames:
            # Add the user to the session
            session['username'] = username
            session['loggedIn'] = True
            return redirect('/')
        else:
            return render_template('loggin.html', message='Invalid username. Please try again.')

    return render_template('loggin.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')



if __name__ == '__main__':
    app.run(debug=True)


