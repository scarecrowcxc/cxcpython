from flask import Blueprint

# 这一步是在干什么：
app_1 = Blueprint('app_1', __name__)

from . import views

