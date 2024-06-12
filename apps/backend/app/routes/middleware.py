
from functools import wraps
from flask import make_response, jsonify

def authenticate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        # Auth check here
        return f(*args, **kwargs)
    return wrapper

def authorize(permission: str):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            # Auth check here
            # current_user = {'permissions': []}
            # permission check here
            # if permission not in current_user['permissions']:
                # return make_response(jsonify({'message': 'Unauthorized'}), 401)
            return f(*args, **kwargs)
        return wrapper
    return decorator