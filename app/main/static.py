from ..utils import logger
from . import main

from ..models import quuestionaire, qadb

from flask import (
    send_from_directory,
    current_app,
)
import os


@main.route("/static/img/<filename>", methods=['GET'])
def get_static_img(filename):
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
    directory = current_app.config.get('BASIC_DIR')  # 获得项目目录
    img_dir = os.path.join(directory, 'app', 'static', 'img')
    return send_from_directory(img_dir, filename, as_attachment=True)


@main.route('/favicon.ico')
def get_icon():
    directory = current_app.config.get('BASIC_DIR')  # 获得项目目录
    img_dir = os.path.join(directory, 'app', 'static', 'img')
    return send_from_directory(img_dir, "icon.png", as_attachment=True)


@main.route("/static/js/<filename>", methods=['GET'])
def get_static_js(filename):
    directory = current_app.config.get('BASIC_DIR')  # 获得项目目录
    img_dir = os.path.join(directory, 'app', 'static', 'js')
    return send_from_directory(img_dir, filename, as_attachment=True)
