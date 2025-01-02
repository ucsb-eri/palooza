# This file should contain records you want created when you run flask db seed.
#
# Example:
# from yourapp.models import User
from palooza.models import Config, Node, Palooza

palooza_dict = {
    "name": "202412",
    "description": "Winter 2024",
}
palooza = Palooza.find_by_name(palooza_dict["name"])
if palooza is None:
    palooza = Palooza(**palooza_dict).save()


node_1 = {"name": "server1", "palooza": palooza}
if Node.find_by_name(node_1["name"]) is None:
    Node(**node_1).save()

node_2 = {
    "name": "server2",
    "palooza": palooza,
}
if Node.find_by_name(node_2["name"]) is None:
    Node(**node_2).save()

current_palooza = {"name": "current_palooza", "value": str(palooza.id)}

if Config.current_palooza() is None:
    Config(**current_palooza).save()
