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

#fibb route

@app.route('/fibonacci/<fnumraw>')
def fibonacci(fnumraw):
    
    fold = 0
    fnew = 1
    fplaceholder = 0
    fnum = 0
    farray = []
    strfarray = ''

    #fnumraw = input("Give me a num ")

    if fnumraw.isdigit():
        fnum = int(fnumraw)
        fplaceholder = fnew + fold    

        if fold < fnum:
            farray.append(fold)
    
        if fnew < fnum:
            farray.append(fnew)

    
        while fplaceholder <= fnum:
            farray.append(fplaceholder)
            fold = fnew
            fnew = fplaceholder
            fplaceholder = fnew + fold
            
        #strfarray = ' '.join(str(e) for e in farray)
        
        return jsonify (
            input = fnumraw,
            
            output = farray
            )

    else:
        return jsonify ("You must input a positive integer")

#md5 route

@app.route('/md5/<text>')
def md5(text):
    
    import hashlib
    from hashlib import md5  
    
    outputtext = text
    textUtf8 = text.encode("utf-8")
    
    
    hash = hashlib.md5( textUtf8 )
    hexa = hash.hexdigest()
    
    #m = hashlib.md5()
    #m.update(text.encode('utf-8'))
    #md5string=m.digest()
    
    return jsonify (
        input = outputtext,
        output = hexa
        )

# is-prime route
@app.route('/is_prime/<num>')
def isprime(num):
    
    if num.isdigit():
        x=True
        inum = num
        num = int(num)
        for i in range(2, num//2):
            if(num % i) ==0:
                x = False
                break
        if x:
            return jsonify (
                input = inum,
                output = True 
            )
        else:
            return jsonify (
                input = inum,
                output = False 
            )
    else: 
        return jsonify ("You must input a positive integer")
   
#factorial route

@app.route('/factorial/<fnum>')
def factorial(fnum):
        
    ifnum = fnum
    
    if fnum == "0":
        return jsonify (
                input = ifnum,
                output = 1 
            )

    elif fnum.isdigit():
        
        fnum = int(fnum)
        x = 1
        sfnum = fnum
        
        while x < fnum:
            sfnum = sfnum * x
            x = x + 1
            
        #sfnum = str(sfnum)
        
        return jsonify (
                input = ifnum,
                output = sfnum 
            )
    

    else:
        return jsonify ("You must input a positive integer") 
 


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
