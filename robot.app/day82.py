# Import the Flask module
from flask import Flask, render_template, request

# Create an instance of the Flask class
app = Flask(__name__)

# Define the default English page
english_page = {
    "title": "Bilingual Challenge",
    "content": "What language are you using? Welcome!",
}

# Define the translated page (you can replace the content with your own translation)
translated_page = {
    "title": "Défi bilingue",
    "content": "Quelle langue utilisez-vous ? Bienvenue!",
}

# Define the route for the default English page
@app.route('/english')
def english():
    return render_template('page.html', data=english_page)

# Define the route for the translated page
@app.route('/otherLanguage')
def other_language():
    return render_template('page.html', data=translated_page)

# Define the route for the default landing page (no language specified)
@app.route('/')
def default_page():
    return render_template('page.html', data=english_page)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
