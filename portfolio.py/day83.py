from flask import Flask, redirect, url_for, request

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

# Define default theme and themes mapping
default_theme = 'default'
themes = {
    'default': 'styles.css',
    'theme1': 'theme1.css',
    'theme2': 'theme2.css',
}

def render_blog(blog_key):
    theme = request.args.get('theme', default_theme)
    css_file = themes.get(theme, themes[default_theme])

    return blog_template.format(
        style=url_for('static', filename=css_file), 
        **blogs.get(blog_key)
        )

@app.route('/hello-world')
def blog1():
    return render_blog('hello-world')

@app.route('/bye-world')
def blog2():
    return render_blog('bye-world')

@app.route('/blog-1')
def r_blog1():
    return redirect(url_for('blog1', theme=request.args.get('theme', default_theme)))

@app.route('/blog-2')
def r_blog2():
    return redirect(url_for('blog2', theme=request.args.get('theme', default_theme)))


# Main execution point
if __name__ == '__main__':
    # Run the Flask app on host '0.0.0.0' and port 8081 in debug mode
    app.run(host='0.0.0.0', port=8081, debug=True)
