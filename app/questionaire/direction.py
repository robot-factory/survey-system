from . import questionaire_blueprint as qb
from ..utils import logger
from flask import (
    request,
    session,
    redirect,
    url_for,
    render_template,
    jsonify,
    send_file,
)
from ..models import (
    quuestionaire,
    answerdata,
    qadb,
)
from bson import ObjectId
import json, os


log = logger(__name__)

# 这部分是关于问卷系统的使用教程和更新日志的

@qb.route('/tutorial')
def tutorial():
    username = session.get('username')
    user_id = session.get('user_id')

    projects = qadb.project_find({'user_id': user_id})

    data_exsample = {
        "username": username,
        "projects": list(projects),
    }
    return render_template('questionaire/tutorial.html',data=data_exsample)