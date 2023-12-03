

from flask import Flask


def init_app():
    app = Flask(__name__)

    with app.app_context():
        from .nse.nse_routes import nse_blues
        from .crypto.crypto_routes import crypto_blues

        app.register_blueprint(nse_blues)
        app.register_blueprint(crypto_blues, url_prefix='/crypto')

        return app
