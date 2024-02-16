from flask import Flask, session, request, render_template, redirect
from models import User, Post

app = Flask(__name__)
app.config['SECRET_KEY'] = '89b1691e-0431-4b7c-9658-2334c0f6d128'

@app.get('/homepage')
def homepage():
    user = None
    if 'USER_ID' in session:
        user = User.get(session['USER_ID'])
    return render_template('index.html', user=user, blogs=Post.all())

@app.get('/signup')
def sign_up():
    return render_template('signup.html')

@app.get('/logout')
def logout():
    session.clear()
    return redirect('login')

@app.post('/signup')
def create_user():
    data = {}
    attrs = ['name', 'username', 'password']
    for attr in attrs:
        if attr in request.form:
            data[attr] = request.form[attr]

    user = User(**data)
    user.save()

    return redirect('login')

@app.get('/')
def blank():
    return redirect('homepage')

@app.get('/login')
def login():
    return render_template('login.html')

@app.post('/login')
def user_auth():
    data = {}
    attrs = ['username', 'password']
    for attr in attrs:
        if attr in request.form:
            data[attr] = request.form[attr]
        
    password = data.pop('password', None)
    user = User.match(**data)
    if user is not None and user.password == password:
        session['USER_ID'] = user.id
        # Redirect to admin page if it's you
        if user.id == "13197838":  # Change this ID to your actual user ID
            return redirect('admin')
        else:
            return "Naughty naughty! You're not allowed here."

    return redirect('login')

@app.get('/admin')
def admin():
    # Check if user is logged in and if it's you
    if 'USER_ID' in session and session['USER_ID'] == "13197838":
        return render_template('admin.html')
    else:
        return redirect('login')

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if 'USER_ID' not in session:
        return redirect('login')
    
    user = User.get(session.get('USER_ID'))
    if not user:
        return redirect('login')
    
    if request.method == 'POST':
        user.name = request.form.get('name')
        user.password = request.form.get('password')
        user.save()
        
        return render_template('edit.html', user=user, message="User details updated successfully.")
    
    return render_template('edit.html', user=user)

@app.post('/blogs')
def create_blog():
    data = {}
    attrs = ['title', 'created_at', 'body']
    for attr in attrs:
        if attr in request.form:
            data[attr] = request.form[attr]

    post = Post(**data)
    post.save()

    return redirect('homepage')

if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=True)
