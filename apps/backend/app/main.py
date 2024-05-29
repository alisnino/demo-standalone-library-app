from flask import Flask, make_response
from models.db import db
from flask_migrate import Migrate

# Tables
from models import book

# Routes
from routes.book import book_route

app = Flask(__name__)
app.register_blueprint(book_route, url_prefix='/books')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///librarysystem.db"

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def health_check():
    return make_response("OK", 200)