from flask import flask

app = Flask(__name__)

@app.route('/is-prime/<num>')

def is_prime(num):
    if num < 2:
        return "Enter number larger than 1"
    else:
        for x in range(2,num):
            if num % x == 0:
               return "Not a prime"
        return "Is a prime"
    #return is_prime 

if __name__ == "__main__":
    app.debug = True 
    app.run('0.0.0.0')
