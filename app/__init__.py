from flask import (
    Flask,
    make_response,
    redirect,
    abort,
    render_template,
    request,
    session,
    url_for, # 视图函数的名字
    flash,
)
from config import config
from app.questionaire import questionaire_blueprint
from app.main import main


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # print(app.config.items())
    app.register_blueprint(main)
    app.register_blueprint(questionaire_blueprint)
    # 模块拓展在这里加入路由

    return app

