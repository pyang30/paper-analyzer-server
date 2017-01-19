class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "paper-analyzer"
    SQLALCHEMY_DATABASE_URI = 'sqlite://:memory:'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:sa@localhost/paper_analyze'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS =True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:sa@localhost/paper_analyze'