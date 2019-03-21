from flask import Flask

app = Flask(__name__)

@app.route('/fibonacci/<int>')
def handle_md5(int):
    
    fold = 0
    fnew = 1
    fplaceholder = 0
    fnum = 0
    farray = []

    fnumraw = input("Give me a num ")

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

        return farray

    else:
        return "You must input a positive integer"
 
    if __name__ =="__main__":
            app.run(debug=True,port=8080)       
#app.debug = True
#app.run()        