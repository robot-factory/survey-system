from ..utils import logger
from . import main
from flask import (
    request,
    render_template,
    url_for,
    jsonify,
    current_app,
    session,
    redirect,
    make_response,
)
from ..models import quuestionaire, qadb
from hashlib import sha1
import json



log = logger(__name__)


@main.route('/')
def index():
    # log.info('index')
    return render_template('main/index.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':

        return render_template('main/login.html')
    if request.method == 'POST':
        secret_key = current_app.config.get('SECRET_KEY')
        username = request.form.get('username')
        account_data = qadb.user_find_one({'username': username})
        if account_data is None:
            return jsonify((False, "The username doesn't existed!"))

        pwd = request.form.get('pwd')
        mix_word = str(secret_key) + str(username) + str(pwd)
        sha = sha1(mix_word.encode('utf-8'))
        sha_pwd = sha.hexdigest()
        if account_data['pwd'] == sha_pwd:
            user_data = {
                'user_id': str(account_data['_id']),
                'username': account_data['username']
            }
            session.update(user_data)
            respose = make_response(redirect(url_for('.project')))
            respose.set_cookie('username', account_data['username'])

            return respose
        else:
            return jsonify((False, '账号或密码错误'))


@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('main/register.html')

    if request.method == 'POST':
        secret_key = current_app.config.get('SECRET_KEY')
        username = request.form.get('username')
        if qadb.user_find_one({'username': username}) is not None:
            return jsonify((False, 'The username has existed!'))
        pwd = request.form.get('pwd')
        mix_word = str(secret_key)+str(username)+str(pwd)
        sha = sha1(mix_word.encode('utf-8'))
        sha_pwd = sha.hexdigest()
        userdata = {}
        userdata['email'] = request.form.get('email')

        result = qadb.user_add(username, sha_pwd, userdata)
        return jsonify((result,))


@main.route('/project')
def project():
    username = session.get('username')
    user_id = session.get('user_id')

    projects = qadb.project_find({'user_id': user_id})

    data_exsample = {
        "username": username,
        "projects": list(projects),
    }
    return render_template('main/project.html', data=data_exsample)


@main.route('/project_add', methods=["POST"])
def project_add():
    project_name = request.form.get('projectname')
    user_id = session.get('user_id')
    if user_id is None:
        return redirect(url_for('login'))
    result = qadb.project_add(user_id, project_name)
    #
    return redirect(url_for('.project'))


@main.route('/project_add_ajax', methods=["POST"])
def project_add_ajax():
    project_name = request.form.get('project-name')
    # print(form_data_json)
    user_id = session.get('user_id')
    if user_id is None:
        return redirect(url_for('login'))
    result = qadb.project_add(user_id, project_name)
    if result:
        # 1代表成功
        return jsonify(1)
    else:
        # 2代表插入失败
        return jsonify(2)