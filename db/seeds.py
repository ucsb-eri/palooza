# This file should contain records you want created when you run flask db seed.
#
# Example:
# from yourapp.models import User
from palooza.models.palooza import Palooza

initial_palooza = {
    'name': '202412',
    'description': 'Winter 2024',
}
if Palooza.find_by_name(initial_palooza['name']) is None:
    Palooza(**initial_palooza).save()
