# Import flask
import flask, requests, json
from flask import Flask

# Setup app
app = Flask(__name__)

# Set up a route
@app.route('/')
def index():
    # Do stuff
    return 'it works'

# Set up more routes here
# is-prime route 
@app.route('/is_prime/<int>')

is_prime = 0
def is_prime(num):
    for i in range(2, num):
        if n%i==0:
            return False 
    return True
return is_prime 

# slack-alert route
@app.route('/send_slack/<string>')
def send_slack(x):
    
    try:
        #change the url depending on the channel you want to post to
        web_hook_url = 'https://hooks.slack.com/services/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'

        #x = 6
        slack_msg = {'text': x }
        requests.post(web_hook_url,data=json.dumps(slack_msg))
        return True

    except invalid_payload:
        #when received request is malformed, text did not properly escape
        return False

    except channel_not_found:
        #channel being addressed doesn't exist or is invalid
        return False

    except channel_is_archived:
        #channel has been archived, no longer recieving messages
        return False
    


# This check will only run the code if you run it from the terminal,
# not if you import it
if __name__ == '__main__':
    # Set debug to true
    # app.debug = True
    # Run the app
    app.run(host='0.0.0.0')
