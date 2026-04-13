from flask import Flask
from config import Config
from models import db


def create_app():
    """Application factory - builds and configures the Flask app"""
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)