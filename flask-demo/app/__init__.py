from flask import Flask

def create_app():
    app = Flask(__name__)

    # 据说这两步就好比django中的主子分发那种感觉
    from .app_1 import app_1 as app_1_blueprint
    app.register_blueprint(app_1_blueprint, url_prefix = '/app_1')

    from .app_2 import app_2 as app_2_blueprint
    app.register_blueprint(app_2_blueprint, url_prefix = '/app_2')

    return app
