from flask import Flask, url_for

# Initialize the Flask application
app = Flask(__name__)

# Define the root route


@app.route('/')
def index():
    return 'Portfolio Project!'

# Define the home route


@app.route('/home')
def home():
    page = """ 
    <!DOCTYPE html>
<html>
  <head>
    <title>My Portfolio Project</title>
    <style>
      .container {
        display: flex;
        align-items: flex-start;
      }

      .text-content {
        flex: 1;
        padding-left: 20px; /* Add some space between the image and text */
      }

      /* Style for the images */
      .image-container {
        display: flex;
        justify-content: space-between; /* Distribute the images evenly */
      }

      .image-container div {
        width: 30%; /* Adjust based on your preference */
        margin-right: 10px; /* Add some space between the images */
      }

      .image-container div img {
        width: 100%;
      }
      .left {
            display: flex;
            justify-content: left;
            align-items: left;
            color: rgb(11, 13, 11);
        }
       h2, h4, h5, h6 {
            color: rgb(12, 14, 13); /* Set text color for all headers */
        }
    </style>
  </head>

  <body>
    <div class="left">
      <h1>Karlie's Portfolio Project</h1>
  </div>
    <div class="container">
      <img src="Karlie.jpg" alt="Karlie Image" width="20%" />
      <div class="text-content">
        <p>
          Hey there! 🌟 My name is Karlie Moyo, a passionate full-stack
          developer hailing from South Africa. Currently, skilled in JavaScript,
          C, Python, Ruby, React, Node.js, and more. Committed to creating
          seamless, user-friendly web experiences. Join me in shaping the
          digital world! 🚀I'm immersed in crafting innovative web applications,
          utilising technologies like Python, Ruby, JavaScript, React, and
          Node.js. I aim to create impactful solutions and enrich the digital
          landscape. Let's collaborate and code something extraordinary! 🚀
        </p>

        <p>
          In my continuous pursuit of skill enhancement and disciplined
          learning, I undertook the '100 Days of Code' challenge. This
          initiative required dedicating a minimum of one hour daily to coding
          tasks and projects for a consecutive 100 days. Throughout this
          journey, I focused on refining my coding capabilities, expanding my
          technical expertise, and developing a consistent work ethic. Engaging
          with a vibrant online community, I shared my progress, collaborated on
          diverse projects, and leveraged feedback to drive continuous
          improvement. This experience not only enriched my programming skills
          but also reinforced my commitment to lifelong learning and
          professional growth.
        </p>

        <h1>What I Have Learned!</h1>
        <ul>
          <li>Greatness is a lot of small things done well</li>
          <li>The salt of patience seasons everything</li>
          <li>Grit alone is not enough develop passion and determination</li>
          <li>
            He who rejects change is the architect of decay. The only human
            institution which rejects progress is the cemetery
          </li>
        </ul>
        <h2>3 Things I am excited about:</h2>
        <ul>
          <li>Skill Enhancement and Mastery</li>
          <li>Achievement and Personal Growth</li>
          <li>Community Engagement and Networking</li>
        </ul>
        <p>Let's Collaborate!</p>
      </div>
    </div>

    <h2>Links to My Achievements Below:</h2>
    <p>
      <a href="https://github.com/Karlie-crypto/Python-100days-tocode-challenge"
        >GitHub Repository</a
      >
    </p>
    <p>
      <a href="https://github.com/Karlie-crypto/Python-100days-tocode-challenge/blob/main/day73-ofcode-challenge"
        >Portfolio1</a>
    </p>
    <p>
      <a href="https://github.com/Karlie-crypto/Python-100days-tocode-challenge/blob/main/day74-ofcode-challenge"
        >Portfolio2</a
      >
    </p>
    <p>
      <a href="https://github.com/Karlie-crypto/Python-100days-tocode-challenge/blob/main/day66-ofcode-challengemain"
        >Calculator</a
      >
    </p>
    <p>
      <a href="https://github.com/Karlie-crypto/Python-100days-tocode-challenge/blob/main/day43-ofcode-challenge"
        >Bingo Card Generator</a
      >
    </p>
    <p>
      <a href="https://github.com/Karlie-crypto/Python-100days-tocode-challenge/blob/main/day69-ofcode-challenge"
        >Visual Novel</a
      >
    </p>
    <a style="color:red;" href="karlie.html">Go to page 2</a>
  </body>
</html>
    """.format(
        css=url_for('static', filename='Templates/styles.css'),
        image=url_for('static', filename='images/Karlie.jpg')
    )
    return page


# Main execution point
if __name__ == '__main__':
    # Run the Flask app on host '0.0.0.0' and port 8080 in debug mode
    app.run(host='0.0.0.0', port=8081, debug=True)
