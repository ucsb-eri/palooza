from flask import Blueprint, jsonify, request
from sqlalchemy import select

from palooza.models import Node

nodes = Blueprint("nodes", __name__)


@nodes.put("/nodes/<id>")
def update_node(id):
    node = Node.query.get(id)

    print(request.json)
    # print(request.)
    updates = request.json
    for key, value in updates.items():
        setattr(node, key, value)
    node.save()
    #
    # print('after')
    return jsonify(node.to_dict())
