# Import flask
import flask
from flask import Flask

# Setup app
app = Flask(__name__)

# Set up a route
@app.route('/')
def index():
    # Do stuff
    return 'it works'

# Set up more routes here


# This check will only run tyhe code if you run it from the terminal,
# not if you import it
if __name__ == '__main__':
    # Set debug to true
    app.debug = true
    # Run the app
    app.run('0.0.0.0')
