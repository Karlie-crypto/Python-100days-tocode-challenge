from flask import Flask, redirect, url_for

app = Flask(__name__)

with open('blog.html', 'r') as f:
    blog_template = f.read()

blogs = {
    'hello-world': {
        'title': 'Hello World!',
        'created_at': 'January 2024',
        'body': 'Day 74: The Portfolio project was designed using HTML and CSS, featuring vibrant colors, stylish alignments, and seamless image-text integration. Serving as both a practice platform and a showcase of achievements, it prioritized user engagement and visual appeal. Through structured HTML tags, CSS styles, and strategic alignments, the portfolio presented information in an organized manner.'
    },
    'bye-world': {
        'title': 'Bye World!',
        'created_at': 'December 2055',
        'body': 'Day 77: Redirects efficiently guide website traffic from one URL to another, preserving SEO and user experience. Blog templates provide a standardized format for creating and publishing blog posts, streamlining content creation and ensuring consistency in design and structure across a blog site.'
    }
}


@app.route('/hello-world')
def blog1():
    return blog_template.format(**blogs.get('hello-world'))

@app.route('/bye-world')
def blog2():
    return blog_template.format(**blogs.get('bye-world'))

@app.route('/blog-1')
def r_blog1():
    return redirect(url_for('blog1'))

@app.route('/blog-2')
def r_blog2():
    return redirect(url_for('blog2'))

# Main execution point
if __name__ == '__main__':
    # Run the Flask app on host '0.0.0.0' and port 8081 in debug mode
    app.run(host='0.0.0.0', port=8081, debug=True)
