from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return """
    <h1>Welcome to My Flask App</h1>
    <p>This is the homepage.</p>
    <a href='/hello'>Say Hello</a><br>
    <a href='/about'>About Us</a><br>
    <a href='/contact'>Contact Us</a>
    """

# Hello World route
@app.route("/hello")
def hello_world():
    return "<h2>Hello, World!</h2><p>This is a simple greeting page.</p>"

# About route
@app.route("/about")
def about():
    return """
    <h2>About Us</h2>
    <p>This Flask app is an example of adding more content.</p>
    <a href='/'>Go Back Home</a>
    """

# Contact route with form submission
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]
        return f"<h2>Thank you, {name}!</h2><p>Your message: {message}</p><a href='/'>Go Back Home</a>"
    return """
    <h2>Contact Us</h2>
    <form method="POST">
        Name: <input type="text" name="name"><br>
        Message: <textarea name="message"></textarea><br>
        <input type="submit" value="Send">
    </form>
    <a href='/'>Go Back Home</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
