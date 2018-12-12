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


@qb.route('/question')
def question():
    qid = request.args.get('qid')
    log.info("qid: "+qid)
    log.info("query result:"+str(quuestionaire.query(qid)))
    return render_template("questionaire/questionaire.html",qid=qid)


@qb.route('/')
def index():
    qid = request.args.get('qid')
    return "please enter your questionaire code!"


@qb.route('/answer', methods=['GET','POST'])
def answer():
    # 信息验证
    qid = request.args.get('qid')
    log.info("qid: " + str(qid))

    if request.method == 'POST':
        # log.info("query result:"+str(quuestionaire.query(qid)))
        if qid is None:
            return '<h1>无问卷编号</h1>'
        if len(request.form) == 0:
            return '<h1>错误数据</h1>'

        # 数据验证
        # todo

        # 数据保存
        datajson = json.dumps(request.form)
        form_data = json.loads(datajson)
        print(form_data)
        result = qadb.data_add(qid,form_data)
        print(result)
        # response = qadb.data_add(qid, form_data)
        return 'success'
    if request.method == 'GET':
        filepath = qadb.data_download(qid)
        return send_file(filepath)


@qb.route('/project_manage')
def project_manage():
    qid = request.args.get('qid')
    project_data = list(qadb.project_find({'_id': ObjectId(qid)}))[0]
    print(dict(project_data))
    return render_template('questionaire/project_manage.html', project= project_data)

@qb.route('/project_edit')
def project_edit():
    # 三个模式：简单模式、自动模式和专业模式
    qid = request.args.get('qid')
    # print(request.get_data())
    return render_template('questionaire/project_edit.html',qid = qid)

@qb.route('/project_edit_add',methods=['POST'])
def project_edit_add():
    qid = request.args.get('qid')
    # 检验是否有资格编辑此问卷
    user_id =session.get('user_id')
    # 有资格后开始添加
    # print(request.get_data())
    try:
        ques = json.loads(request.get_data().decode('utf-8'))
        # result = qadb.ques_add(qid,ques)
        project_data = qadb.ques_get(qid)
        # 判断有误权限
        if project_data['user_id']==user_id:
            result = qadb.ques_add(qid,ques)
        else:
            result = "no permission!"
        print(result)
    except Exception as e:
        print(e)
    return "ok"

@qb.route('/project_edit_get')
def project_edit_get():
    qid = request.args.get('qid')
    user_id =session.get('user_id')
    try:
        project_data = qadb.ques_get(qid)
        # 判断有误权限
        if project_data['user_id'] == user_id:
            result = json.dumps(project_data['ques'])
        else:
            result = "No permission!"
    except Exception as e:
        print(e)
        result = "fault!"
    # print(result)
    return result