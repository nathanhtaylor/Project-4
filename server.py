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
# is-prime route 
@app.route('/is_prime/<int>')

is_prime = 0
def is_prime(num):
    for i in range(2, num):
        if n%i==0:
            return False 
    return True
return is_prime 


#This route returns all fibonacci numbers
#less than or equal to the input
@app.route('/fibonacci/<fnumraw>')
def fibonacci(fnumraw):
    
    #initialization of variables
    fold = 0
    fnew = 1
    fplaceholder = 0
    fnum = 0
    farray = []
    strfarray = ''

    #this block executes if the input is a positive integer
    if fnumraw.isdigit():
        #converts the input to an int
        fnum = int(fnumraw)
        #this just deals with the fibonacci part
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
         
        #converts the array to a series of strings, then returns it
        strfarray = ' '.join(str(e) for e in farray)
        return strfarray
    
    #this error message executes if the input is not a positive integer
    else:
        return "You must input a positive integer"
 
      

app.run() 

# This check will only run the code if you run it from the terminal,
# not if you import it
if __name__ == '__main__':
    # Set debug to true
    # app.debug = True
    # Run the app
    app.run(host='0.0.0.0')
