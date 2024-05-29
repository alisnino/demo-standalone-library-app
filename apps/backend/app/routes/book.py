from flask import Blueprint

book_route = Blueprint('book', __name__)

@book_route.route('/', methods=['GET'])
def get_books():
    return "This is the book API!"
