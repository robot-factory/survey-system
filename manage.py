import os
from app import create_app
from flask_script import Manager, Command, Option, Server


# app = create_app("default")
# manager = Manager(app)


manager = Manager(create_app)
manager.add_option("-c", "--config_name", dest="config_name", required=False)
# 输入模式是开发、生成还是测试





if __name__ == '__main__':
    manager.run()
    # python manage.py -c development runserver -d -r -p 8000 -h 0.0.0.0
    # -c必须放前面因为是给create_app的函数
    # --threaded  # 开启多线程
    # -d  # 开启调试模式
    # -r  # 自动加载
    # -h，--host  # 指定主机
    # -p，--port  # 指定端口
    # -D --NO-DEBUG 关闭调试