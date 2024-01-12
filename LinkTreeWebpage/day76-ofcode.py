
from flask import Flask, url_for

# Initialize the Flask application
app = Flask(__name__)

# Define the root route


@app.route('/')
def index():
    return 'Link Tree Project!'

# Define the home route


@app.route('/home')
def home():
    page = """ 
    <!DOCTYPE html>
    <html>
    <head>
        <title>Link Tree</title>
        <!-- Link to the stylesheet -->
        <link rel="stylesheet" href="{css}">
    </head>
    <body>
        <div class="flex-container">
            <!-- Adjusted the image source path -->
            <img src="{image}" alt="Karlie Moyo Image">
            <h1>Karlie Moyo</h1>
            <h3>Socials</h3>
            <ul>
                <li><a href="https://github.com/Karlie-crypto">Github</a></li>
                <li><a href="https://www.linkedin.com/in/karlie-moyo">LinkedIn</a></li>
                <li><a href="https://twitter.com/karlieemoyo">Twitter</a></li>
                <li><a href="https://medium.com/me/stories/public">Medium</a></li>
            </ul>
            <p>Karlie Moyo is a distinguished Software Engineer with a B.Sc. in Full Stack Software Engineering from Southampton University and a Backend Certification from ALX. A participant in Replit's 100-day coding challenge, she exemplifies dedication and expertise, heralding the dawn of an illustrious career marked by unparalleled excellence. 
                Currently, she is actively involved in a blockchain project and has developed numerous websites and mobile applications. Notably, she has contributed to projects addressing mental health concerns among the youth, exemplified by her work on Kamva MindPal.
            </p>
        </div>
    </body>
    </html>
    """.format(
        css=url_for('static', filename='Templates/styless.css'),
        image=url_for('static', filename='images/KarlieMoyo.jpg')
    )
    return page


# Main execution point
if __name__ == '__main__':
    # Run the Flask app on host '0.0.0.0' and port 8080 in debug mode
    app.run(host='0.0.0.0', port=8080, debug=True)
