'''
write code for main.py
creating a simple Flask application that serves a "Hello, World!" message at the root endpoint.
'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'