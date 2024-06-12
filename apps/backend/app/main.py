from functools import wraps
from flask import Flask, make_response
from models.db import db
from flask_migrate import Migrate

# Tables
from models import books

# Routes
from routes.auth import auth_route
from routes.books import books_route

app = Flask(__name__)
app.register_blueprint(auth_route, url_prefix='/auth')
app.register_blueprint(books_route, url_prefix='/books')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///librarysystem.db"

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def health_check():
    return make_response("OK", 200)