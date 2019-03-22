# Import flask
import flask, requests, json
from flask import Flask, jsonify

#from flask_api import status

# Setup app
app = Flask(__name__)

# Set up a route
@app.route('/')
def index():
    # Do stuff
    return 'it works and it works and it works a third time'

# Set up more routes here
# is-prime route
@app.route('/is_prime/<int:num>')

def is_prime(num):
    num = int(num)
    if num < 2:
        return 'Enter number larger than 1'
    else:
        for x in range(2,num):
            if num % x == 0:
               return 'Not a prime'
        return 'Is a prime'
   
#factorial route
#needs more testing, may not be fully functional
@app.route('/factorial/<string:num>', methods=['GET'])
#def factorial(num):
    #try:
        #x = int(num)
    #except ValueError
        #return jsonify(formatted_return(num, "ERROR: Integer value expected.")), status.HTTP_400_BAD_REQUEST
    #result = x
    #if x > 0:
        #count = x - 1
        #while count > 0:
            #result *= count
            #count -= 1
        #return jsonify(formatted_return(num, result))
    #else:
        #return jsonify(formatted_return(num, "ERROR: Integer must be greater than zero.")), status.HTTP_400_BAD_REQUEST

# slack-alert route
@app.route('/send_slack/<string:x>')
def send_slack(x):
    
    #print("Input: ", x)

    #change the url depending on the channel you want to post to
    web_hook_url = 'https://hooks.slack.com/services/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'

    #x = 6
    slack_msg = {'text':x}
    requests.post(web_hook_url,data=json.dumps(slack_msg))
    return jsonify(
        input=x,
        output=True
    )


# This check will only run the code if you run it from the terminal,
# not if you import it
if __name__ == '__main__':
    # Set debug to true
    # app.debug = True
    # Run the app
    app.run(host='0.0.0.0')
