from flask import Blueprint, jsonify
from sqlalchemy import select
from palooza.models import Palooza, Config

paloozas = Blueprint('paloozas', __name__)

@paloozas.get('/paloozas')
def show():
    current_palooza = Config.current_palooza()

    # print(current_palooza)
    palooza= Palooza.query.filter_by(id=current_palooza).one_or_none()
    # print('here')
    print(palooza)
    #
    # print('after')
    return jsonify(palooza.to_dict())
