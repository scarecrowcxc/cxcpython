from flask import render_template

# 这里从当前文件夹下导入了auth 蓝图吧？
from . import auth


@auth.route('/login')
def login():
    return render_template('auth/login.html')
