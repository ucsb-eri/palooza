from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from palooza.api import index

class Base(DeclarativeBase):
    pass

def main():
    app = Flask(__name__, static_folder='frontend/dist', static_url_path="/")
    app.register_blueprint(index, url_prefix='/api')

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        return app.send_static_file("index.html")

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    db = SQLAlchemy(model_class=Base)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # @app.route('/')
    # def hello():
    #     return 'Hello from Flask!'
    

    app.run(host='0.0.0.0', port=1234, debug=True)
