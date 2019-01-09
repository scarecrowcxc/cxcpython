from flask import render_template, session, redirect, url_for, current_app, flash
from . import main
from .forms import NameForm

# 加入数据库后要依赖的包
from .. import db
from ..models import User

# 加入发送邮件功能要依赖的包
from ..email import send_email



#加入web表单的版本
#@main.route('/', methods=['Get', 'POST'])
#def index():
#    form = NameForm()
#    if form.validate_on_submit():
#        old_name = session.get('name')
#        if old_name is not None and old_name != form.name.data:
#            flash('Looks like you have changed your name!')
#        session['name'] = form.name.data
#        return redirect(url_for('.index'))
#    return render_template('index.html', form=form, name=session.get('name'))



# 加入数据库的版本
@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            if current_app.config['FLASKY_ADMIN']:
                send_email(current_app.config['FLASKY_ADMIN'], 'New User', 'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))




# 这里的运行已经移动到了 manage.py 文件中了
#if __name__ == '__main__':
#    manager.run()
