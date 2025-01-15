import traceback

from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from ldap3 import ALL, SUBTREE, Connection, Server
from ldap3.core.exceptions import LDAPBindError
from flask import current_app

login = Blueprint("login", __name__)


@login.post("/login")
def login_post():
    server = current_app.config["LDAP_URI"]

    root_dn = "OU=GRIT Users,DC=grit,DC=ucsb,DC=edu"

    username = request.json.get("username", None)
    password = request.json.get("password", None)

    user = f"cn={username},{root_dn}"

    server = Server(server, get_info=ALL)

    try:
        connection = Connection(server, user=user, password=password, auto_bind=True)

        results = connection.search(
            search_base=f"CN={username},OU=GRIT Users,DC=grit,DC=ucsb,DC=edu",
            search_filter="(objectClass=user)",
            search_scope=SUBTREE,
            attributes=["memberOf"],
        )

        groups = connection.response[0]["raw_attributes"]["memberOf"]

        if b"CN=palooza,OU=GRIT Users,DC=grit,DC=ucsb,DC=edu" in groups:
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token)
        else:
            return jsonify({"msg": "The user does not have access to the required group"}), 401

    except LDAPBindError as e:
        traceback.print_exc()
        return jsonify({"msg": "Invalid username or password"}), 401
