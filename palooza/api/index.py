from flask import Blueprint, jsonify
from sqlalchemy import select
from palooza.models.palooza import Palooza

index = Blueprint('index', __name__)

@index.route('/', defaults={'page': 'index'})
@index.route('/<page>')
def show(page):
    paloozas= Palooza.query.all()
    print('here')
    print(paloozas)

    print('after')
    return jsonify([el.to_dict() for el in paloozas])
