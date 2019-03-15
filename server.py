# Import flask
import flask, requests
from flask import Flask

# Setup app
app = Flask(__name__)

# Set up a route
@app.route('/')
def index():
    # Do stuff
    return 'it works'

# Set up more routes here


# This check will only run the code if you run it from the terminal,
# not if you import it
if __name__ == '__main__':
    # Set debug to true
    # app.debug = True
    # Run the app
    app.run(host='0.0.0.0')
