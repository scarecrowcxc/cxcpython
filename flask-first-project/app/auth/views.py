from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from .. models import User
from .forms import LoginForm
# 这里从当前文件夹下导入了auth 蓝图吧？
from . import auth


@auth.route('/login', method=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.fliter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data)
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password')
    return render_template('auth/login.html', form=form)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))



