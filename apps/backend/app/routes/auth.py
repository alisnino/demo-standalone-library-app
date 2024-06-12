from flask import Blueprint, request, make_response, jsonify

auth_route = Blueprint('auth', __name__)

@auth_route.route('/login', methods=['POST'])
def login():
    username, password = request.json['username'], request.json['password']
    # if not both exist make response with bad request
    if not username or not password:
        return make_response(jsonify({'message': 'Bad request'}), 400)
    return make_response(jsonify({'message': 'Login success'}), 200)