# Import flask
import flask, requests
from flask import Flask

# Setup app
app = Flask(__name__)

# Set up a route
@app.route('/')
def index():
    # Do stuff
    return 'it works (test)'

@app.route('/test/')
def index():
    # Do stuff
    return 'it works here too'

# Set up more routes here
# is-prime route
@app.route('/is_prime/<num>')

def is_prime(num):
    num = int(num)
    if num < 2:
        return 'Enter number larger than 1'
    else:
        for x in range(2,num):
            if num % x == 0:
               return 'Not a prime'
        return 'Is a prime'

# This check will only run the code if you run it from the terminal,
# not if you import it
if __name__ == '__main__':
    # Set debug to true
    # app.debug = True
    # Run the app
    app.run(host='0.0.0.0')
