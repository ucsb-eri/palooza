from flask import Blueprint

from sqlalchemy import select
from palooza.models.palooza import Palooza

index = Blueprint('index', __name__)

@index.route('/', defaults={'page': 'index'})
@index.route('/<page>')
def show(page):
    return Palooza.query.all()
