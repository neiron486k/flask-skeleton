class DefaultConfig:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevConfig(DefaultConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/flask'


class ProdConfig(DefaultConfig):
    DEBUG = False
