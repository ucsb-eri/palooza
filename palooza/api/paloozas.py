from flask import Blueprint, jsonify

from palooza.models import Config, Palooza

paloozas = Blueprint("paloozas", __name__)


@paloozas.get("/paloozas")
def show():
    current_palooza = Config.current_palooza()

    palooza = Palooza.query.filter_by(id=current_palooza).one_or_none()

    return jsonify(palooza.to_dict())
