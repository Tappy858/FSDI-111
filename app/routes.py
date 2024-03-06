# Import the Flask class from the Flask module
from flask import Flask

# OOP - Object Oriented Paradigm
# Create an instance of the Flask class with the name of the current module as the argument
# This is a common Flask convention to determine the root path for the application
app = Flask(__name__)

# Flask decorator that maps routes to view functions
# In this case, it maps the root URL '/' to the index function
@app.get("/")
def index():
    # Define a dictionary containing personal information
    me = {
        "first_name": "Darius",
        "last_name": "Tap",
        "hobbies": "Fishing",
        "online": True
    }

    # Return the dictionary as a JSON response
    # Flask automatically converts the Python dictionary to JSON format
    return me