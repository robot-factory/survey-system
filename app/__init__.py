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
from app.analysis import analysis


def create_app(config_name='default'):
    if config_name is None:
        config_name='default'
    # print('config_name',config_name)
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # print(app.config.items())
    app.register_blueprint(main)
    app.register_blueprint(questionaire_blueprint)
    app.register_blueprint(analysis)
    # 模块拓展在这里加入路由

    return app

