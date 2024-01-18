from flask import Flask, render_template

app = Flask(__name__)

reflections = {
    "day1": {
        "title": "Day 1 - Getting Started",
        "repl_link": "https://github.com/Karlie-crypto/Python-100days-tocode-challenge/blob/main/day1-ofcode-challenge",
        "content": "On October 27, I made a promise to be consistent and complete the 100 days of code challenge, look at where we are now! Amazing.",
    },
    "day2": {
        "title": "Day 2 - Exploring print function",
        "repl_link": "https://github.com/Karlie-crypto/Python-100days-tocode-challenge/blob/main/day2-ofcode-challenge",
        "content": "Very interesting, print function is more fun and it makes life easy😄",
    },
    
}

@app.route('/')
def home():
    return "Welcome to the 100 Days of Code Reflections homepage!"

@app.route('/day1')
def index_day1():
    return render_template('reflections.html', **reflections['day1'], day_number=1)

@app.route('/day2')
def index_day2():
    return render_template('reflections.html', **reflections['day2'], day_number=2)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)

