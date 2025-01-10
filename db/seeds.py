# This file should contain records you want created when you run flask db seed.
#
# Example:
# from yourapp.models import User
from palooza.models import Config, Node, Palooza

palooza_1_dict = {
    "name": "202412",
    "description": "Winter 2024",
}
palooza_1 = Palooza.find_by_name(palooza_1_dict["name"])
if palooza_1 is None:
    palooza_1 = Palooza(**palooza_1_dict).save()

palooza_2_dict = {
    "name": "202506",
    "description": "Summer 2025",
}
palooza_2 = Palooza.find_by_name(palooza_2_dict["name"])
if palooza_2 is None:
    palooza_2 = Palooza(**palooza_2_dict).save()


node_1 = {
    "name": "server1",
    "os_name": "fedora",
    "os_version": "41 (Forty One)",
    "paloozas": [palooza_1, palooza_2],
}
if Node.find_by_name(node_1["name"]) is None:
    Node(**node_1).save()

node_2 = {
    "name": "server2",
    "os_name": "ubuntu",
    "os_version": "24.04",
    "paloozas": [palooza_1, palooza_2],
}
if Node.find_by_name(node_2["name"]) is None:
    Node(**node_2).save()

node_3 = {
    "name": "server3",
    "os_name": "centos",
    "os_version": "7 (Core)",
    "paloozas": [palooza_1, palooza_2],
}
if Node.find_by_name(node_3["name"]) is None:
    Node(**node_3).save()

current_palooza = {"name": "current_palooza", "value": str(palooza_1.id)}

if Config.current_palooza() is None:
    Config(**current_palooza).save()
