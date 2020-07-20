# Create a New Python File and Import the Flask Dependency
from flask import Flask
# Create a New Flask App Instance (Create a Flask app)
app = Flask(__name__)

# Create a Flask route
@app.route('/')
def hello_world():
	return 'Hello world'

# forward slash: denote we want to put our data at the root of our routes. 
# Starting point is called root 

# Run a Flask App
# 1) use the command line to navigate to the folder where we’ve saved our code
    #export FLASK_APP=app.py on terminal
    # flask run on the terminal