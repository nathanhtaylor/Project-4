# Import flask
import flask, requests, json
from flask import Flask

# Setup app
app = Flask(__name__)

# Set up a route
@app.route('/')
def index():
    # Do stuff
    return 'it works and it works and it works a third time'

# Set up more routes here
# is-prime route
@app.route('/is_prime/<num>')

def is_prime(num):
    if num < 2:
        return 'Enter number larger than 1'
    else:
        for x in range(2,num):
            if num % x == 0:
               return 'Not a prime'
        return 'Is a prime'
   
# slack-alert route
@app.route('/send_slack/<string>')
def send_slack(x):
    
    print("Input: ", x)

    #change the url depending on the channel you want to post to
    web_hook_url = 'https://hooks.slack.com/services/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'

    #x = 6
    slack_msg = {'text': x }
    requests.post(web_hook_url,data=json.dumps(slack_msg))
    return True


# This check will only run the code if you run it from the terminal,
# not if you import it
if __name__ == '__main__':
    # Set debug to true
    # app.debug = True
    # Run the app
    app.run(host='0.0.0.0')
