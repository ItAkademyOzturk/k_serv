from server import app
from flask import jsonify
from server import db
from server import Signboard
@app.route('/')
def hello_world():
    return jsonify({"message": "hello world"})

@app.route('/signboard/<string:customer_code>/<string:signboard_code>/', methods=['GET'])
def show_signboard(customer_code, signboard_code):
    s = Signboard.query.all()
    
#     # show the post with the given id, the id is an integer
    return jsonify({"signboard": s})