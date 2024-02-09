from flask import Flask, session, request, render_template, redirect
from models import User, Post, Comment

app = Flask(__name__)
app.config['SECRET_KEY'] = '89b1691e-0431-4b7c-9658-2334c0f6d128'

@app.get('/homepage')
def homepage():
    if 'USER_ID' not in session:
        user = None
    else:
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
    # get user data from form
    data = {}
    attrs = ['name', 'username', 'password']
    for attr in attrs:
        if attr in request.form:
            data.update({attr: request.form.get(attr)})

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
    # get login data from form
    data = {}
    attrs = ['username', 'password']
    for attr in attrs:
        if attr in request.form:
            data.update({attr: request.form.get(attr)})
        
    password = data.pop('password', None)
    user = User.match(**data)
    if user is not None and user.password == password:
        session['USER_ID'] = user.id
        # Redirect to edit page instead of homepage
        return redirect('edit')

    return redirect('login')

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    # Check if user is logged in
    if 'USER_ID' not in session:
        return redirect('login')
    
    user = User.get(session.get('USER_ID'))
    if not user:
        return redirect('login')
    
    if request.method == 'POST':
        # Update user data
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
            data.update({attr: request.form.get(attr)})

    post = Post(**data)
    post.save()

    return redirect('homepage')

if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=True)
