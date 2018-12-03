from . import questionaire_blueprint as qb
from ..utils import logger
from flask import (
    request,
    session,
    redirect,
    url_for,
    render_template,
    jsonify,
)
from ..models import (
    quuestionaire,
    answerdata,
    qadb,
)
from bson import ObjectId


log = logger(__name__)


@qb.route('/question')
def question():
    qid = request.args.get('qid')
    log.info("qid: "+qid)
    log.info("query result:"+str(quuestionaire.query(qid)))
    if qid is not None and quuestionaire.query(qid):
        return render_template("questionaire/questionaire.html")
    else:
        return redirect(url_for('.index'))


@qb.route('/')
def index():

    return "please enter your questionaire code!"


@qb.route('/answer', methods=['POST'])
def answer():
    # 信息验证
    qid = request.args.get('qid')
    log.info("qid: " + str(qid))
    log.info("query result:"+str(quuestionaire.query(qid)))
    if qid is None:
        return jsonify((False, "未知问卷"))
    if len(request.form) == 0:
        return jsonify((False, "未提交数据"))

    # 数据验证
    # todo

    # 数据保存
    form_data = {key: value for key, value in request.form.items()}
    response = qadb.data_add(qid, form_data)
    return jsonify(response)

@qb.route('/project_manage')
def project_manage():
    qid = request.args.get('qid')
    project_data = list(qadb.project_find({'_id': ObjectId(qid)}))[0]
    print(dict(project_data))
    return render_template('questionaire/project_manage.html', project= project_data)

