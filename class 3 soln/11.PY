'''
Create a Flask application which listens to port 30000 and has 2 routes:
DevOps Course
Assignment
Lesson 3

www.globaldevexperts.com | hello@globaldevexperts.com
• /content - which returns the content of any txt file and status code 200 (e.g:
localhost:4000/content).
• /register - which writes the word “hello” into any txt file and return “success” and
status code 201 as a response (e.g: localhost:4000/register).

'''
from flask import Flask

app = Flask(__name__)

# Route 1: Home route
@app.route('/')
def home():
    return "Welcome to the Home Page!"

# Route 2: register route
@app.route('/register')
def register():
    return "This is the registration Page."

# Route 2: About route
@app.route('/content')
def content():
    return "This is the content Page."

if __name__ == '__main__':
    # Run the Flask app on port 30000
    app.run(host='0.0.0.0', port=30000)


'''
I do not understand the below, kindly help

/content - which returns the content of any txt file and status code 200 (e.g:
localhost:4000/content).
• /register - which writes the word “hello” into any txt file and return “success” and
status code 201 as a response (e.g: localhost:4000/register).

'''