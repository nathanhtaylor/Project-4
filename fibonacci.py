from flask import Flask

app = Flask(__name__)

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
            
        strfarray = ' '.join(str(e) for e in farray)
        return strfarray

    else:
        return "You must input a positive integer"
 
      
#app.debug = True
app.run()        