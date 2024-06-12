from flask import Blueprint, make_response, jsonify, request
from routes.middleware import authenticate, authorize
from models.books import Book
from models.db import db

books_route = Blueprint('books', __name__)

@authenticate
@authorize('readBooks')
@books_route.route('/', methods=['GET'])
def get_books():
    books = Book.query.all()
    books = [book.to_dict() for book in books]
    return make_response(jsonify(books), 200)

@authenticate
@authorize('writeBooks')
@books_route.route('/register', methods=['POST'])
def register_book():
    title, author, publisher, year, status = request.json['title'], request.json['author'], request.json['publisher'], request.json['year'], request.json['status']
    
    # Start transaction
    db.session.begin()
    new_book = Book(
        title=request.json['title'],
        author=request.json['author'],
        publisher=request.json['publisher'],
        year=request.json['year'],
        status=request.json['status']
    )
    db.session.add(new_book)
    db.session.commit()
    
    return make_response(jsonify(new_book.to_dict()), 201)