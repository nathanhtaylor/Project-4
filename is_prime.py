from flask import flask

app = Flask(__name__)

@app.route('/is-prime/<int>')

is_prime = 0
def is_prime(num):
    for i in range(2, num):
        if n%i==0:
            return False 
    return True
return is_prime 

if __name__ == "__main__":
    app.debug = True 
    app.run('0.0.0.0')