

from flask import flask

from flask import jsonify

from flask import status

app = Flask(__name__)

@app.route('/factorial/<string:num>', methods=['GET'])
def factorial(num):
    try:
        x = int(num)
    except ValueError
        return jsonify(formatted_return(num, "ERROR: Integer value expected.")), status.HTTP_400_BAD_REQUEST
    result = x
    if x > 0:
        count = x - 1
        while count > 0:
            result *= count
            count -= 1
        return jsonify(formatted_return(num, result))
    else:
        return jsonify(formatted_return(num, "ERROR: Integer must be greater than zero.")), status.HTTP_400_BAD_REQUEST


if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0')