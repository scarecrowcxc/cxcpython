from flask import render_template, session, redirectl, url_for, current_app


@mail.route('/')
def index():
    return render_template('index.html')
