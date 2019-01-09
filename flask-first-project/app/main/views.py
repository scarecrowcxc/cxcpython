from flask import render_template, session, redirectl, url_for, current_app
from . import main
from .forms import NameForm


@mail.route('/', methods=['Get', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html', form=form, name=session.get('name'))


# 这里的运行已经移动到了 manage.py 文件中了
#if __name__ == '__main__':
#    manager.run()
