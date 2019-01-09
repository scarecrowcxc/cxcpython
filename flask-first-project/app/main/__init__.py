from flask import Blueprint

# 这里在干什么：这是在子app里面 给自己的app起名字吧～？
# 这是在把这个文件夹变成一个蓝图（子app）
main = Blueprint('main', __name__)

# 这里为什么要导入这两个文件呢？
from .import views, errors
