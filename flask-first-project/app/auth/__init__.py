from flask import Blueprint

auth = Blueprint('auth', __name__)


# 这个导包写在这里是因为 为了避免循环导包
# 因为 在views中 会导入auth 这个蓝图包
from . import views
