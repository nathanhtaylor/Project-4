

from flask import flask 

app = flask(__name__)

@app.route('/md5/<md5string>', methods=['GET'])
    def strings(md5string):
        return(
            output = hashlib.md5(md5string)   
        )

