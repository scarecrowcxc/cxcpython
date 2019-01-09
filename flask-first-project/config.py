import os
basedir = os.path.abspath(os.path.dirname(__file__))


# 创建一个基础类
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess srting'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 发邮件的配置项先空着

    # 这个地方是在干什么 不懂
    @staticmethod
    def init_app(app):
        pass


# 创建三个类
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')or \
            'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


# 接下来还需要定义两个类， 用来测试和生产环境的数据库


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
}
