from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail  import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

# 这是一个工厂函数 用来创建我们的app
# app的初始化是放在这里的
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)
    mail.init_app(app)

    # 这里现在把我们创建的main文件夹注册成一个app(子)
    # 现在这里只有这个名为main的app，后续如果要新增app
    # 都需要在这个地方像这样一样来注册成一个蓝图（子app）
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app