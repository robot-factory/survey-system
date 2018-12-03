from flask_mongoengine import (
    MongoEngine,
)
from flask import (
    current_app,
)
from pymongo import MongoClient
from bson import ObjectId
import datetime
import time
# from ..utils import


class QAHandler:
    # todo
    def __init__(self):
        # mconf = current_app.config.get('QA_DB')
        # todo： 待完善
        mconf = {
            'host': "localhost",
            'port': 27017,
            'dbname': "qa_db",
        }
        self.mongo_client = MongoClient(host=mconf['host'], port=mconf['port'])
        self.db = self.mongo_client[mconf['dbname']]
        # 有三个表：总表包含每个项目项目名、问卷数据库、答案数据库和一些项目信息（创建时间、开始时间、结束时间、是否进行、是否结束）
        # 问卷数据库包含题目和答案类型
        # 答案数据库包含各种
        self.project_col = 'project'
        self.users_col = 'users'

    def user_add(self, username, pwd, userdata):
        #
        col_users = self.db[self.users_col]
        data = {
            'username': username,
            'pwd': pwd,
        }
        data.update(userdata)
        result = col_users.insert_one(data)
        return result.acknowledged

    def user_find(self, *args, **kwargs):
        return self.db[self.users_col].find(*args, **kwargs)

    def user_find_one(self, *args, **kwargs):
        return self.db[self.users_col].find_one(*args, **kwargs)

    def project_add(self, user_id, project_name):
        #
        create_time = int(time.time()*1000)
        create_time_str = str(datetime.datetime.now())
        project_data = {
            'project_name': project_name,
            'user_id': user_id,
            'ct': create_time_str,
            'c_ts': create_time,
            'u_ts': create_time,
            'ut': create_time_str,
            'status': 0,
        }
        col_project = self.db[self.project_col]
        result = col_project.insert_one(project_data)
        insert_id = str(result.inserted_id)
        insert_data = {
            'data_db': 'data_db_'+insert_id,
            'ques_db': 'ques_db_'+insert_id,
            'qid': insert_id,
        }
        col_project.update(
            {'_id': result.inserted_id},
            {'$set': insert_data}
        )
        return True

    def project_find(self, *args, **kwargs):
        return self.db[self.project_col].find(*args, **kwargs)

    def get_data_collection(self, qid):
        document = self.db[self.project_col].find_one({'qid': qid})
        if document is None:
            return None
        else:
            return document.get('data_db')

    def data_add(self, qid, form_data):
        data_db_name = self.get_data_collection(qid)
        if data_db_name is None:
            return False, "No such qid!"
        try:
            self.self.db[data_db_name].insert_one(form_data)
            result = (True,)
        except Exception as e:
            result = (False, e)
        return result

    def data_download(self, qid):
        pass

    def ques_add(self, ques_list):
        pass

    def ques_update(self, ):
        pass







class Questionaires():
    def __init__(self):
        self.qid_list = ["aabbccdd"]

    def add_questionaire(self, qid):
        self.qid_list.append(qid)

    def query(self, query_id):
        return query_id in self.qid_list

class Answerdata():
    def __init__(self):
        pass

    def saveadata(self, qid, data):
        pass

    def getdata(self):
        pass



quuestionaire = Questionaires()
answerdata = Answerdata()
mongo = MongoEngine()
qadb = QAHandler()
# print(current_app.config)