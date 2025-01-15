from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from flask_cors import CORS
from palooza.models import *
import tomllib

from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__, static_folder="frontend/dist", static_url_path="/app")
    app.config.from_file("config.toml", load=tomllib.load, text=False)
    CORS(app, origins=["http://localhost:5173"])
    jwt = JWTManager(app)
    # print(db.)
    db.init_app(app)
    # print(db.engine)

    from palooza.api import login, nodes, paloozas

    app.register_blueprint(login, url_prefix="/api")
    app.register_blueprint(nodes, url_prefix="/api")
    app.register_blueprint(paloozas, url_prefix="/api")

    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def catch_all(path):
        return app.send_static_file("index.html")

    with app.app_context():
        # print(db.metadata)
        db.create_all()

    return app


# def seed():
#     from sqlalchemyseed import load_entities_from_yaml
#     from sqlalchemyseed import Seeder
#
#     with app.app_context():
#         db.create_all()
#
#     app.run(host="0.0.0.0", port=1234, debug=True)
#
#     entities = load_entities_from_yaml(
#         "/home/tjaart/Code/local/palooza/palooza/data.yml"
#     )
#     seeder = Seeder(db.session)
#
#     seeder.seed(entities)
#
#     db.session.commit()
#


def main():
    app = create_app()
    app.run(host="0.0.0.0", port=1234, debug=True)

    # @app.route('/')
    # def hello():
    #     return 'Hello from Flask!'
