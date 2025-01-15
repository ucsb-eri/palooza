from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from palooza.models import Node

nodes = Blueprint("nodes", __name__)


@nodes.put("/nodes/<id>")
@jwt_required()
def node_put(id):
    node = Node.query.get(id)

    updates = request.json
    for key, value in updates.items():
        setattr(node, key, value)
    node.save()

    return jsonify(node.to_dict())
