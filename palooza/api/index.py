from flask import Blueprint

index = Blueprint('index', __name__)

@index.route('/', defaults={'page': 'index'})
@index.route('/<page>')
def show(page):
    return "Hello world"
