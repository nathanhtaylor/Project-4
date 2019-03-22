from flask import Flask

app = Flask(__name__)

@app.route('/factorial/<fnum>')
def fibonacci(fnum):
        

    if fnum == "0":
        return "1"

    elif fnum.isdigit():
        
        fnum = int(fnum)
        x = 1
        sfnum = fnum
        
        while x < fnum:
            sfnum = sfnum * x
            x = x + 1
            
        sfnum = str(sfnum)
        return sfnum
    

    else:
        return "You must input a positive integer"
 
      
#app.debug = True
app.run()