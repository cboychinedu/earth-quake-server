#!/usr/bin/env python3 

# Importing the necessary modules 
import os 
from flask import Flask, url_for 
from flask_cors import CORS 
from flask import send_file; 


# Creating the flask application 
app = Flask(__name__); 
app.config["TEMPLATES_AUTO_RELOAD"] = True 

# Adding the cross-origin 
CORS(app) 

# Setting the json route 
@app.route('/data', methods=["GET", "POST"])
def QuakeData():
    # Return the json data 
    return send_file("static/data/data.json", attachment_filename="data.json")
    

# Handling custom error pages
@app.errorhandler(404)
def page_not_found(e):
    # Execute this route if the user navigates to a route that does not exist
    # return render_template('404.html'), 404;
    return "Error 404", 404; 

# Handling error request 500
@app.errorhandler(500)
def internal_server_error(e):
    # Execute this route if the request generated gives an internal server error
    # return render_template('500.html'), 500;
    return "Bad Request, try againn", 500; 

# Adding functions for updating the web application on reload
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

# Creating a function called dated url for tracking the changes made
def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


# Running the flask application 
if __name__ == "__main__": 
    app.run(); 