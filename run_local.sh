#!/bin/bash

# Set the FLASK_APP environment variable to the path of your main application file
export FLASK_APP=app.routes
# Use 'development' mode for debugging
export FLASK_ENV=development

# Run the Flask application
flask run --debug