from flask import Flask
from flask_talisman import Talisman

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'

    Talisman(app)

    from .routes import main  # ✅ this works now because circular import is gone
    app.register_blueprint(main)

    return app


