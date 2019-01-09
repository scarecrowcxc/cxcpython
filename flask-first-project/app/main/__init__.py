from flask import Blueprint

# 这里在干什么：这是在子app里面 给自己的app起名字吧～？
main = Blueprint('main', __name__)

from .import views, errors
