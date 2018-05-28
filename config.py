import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """
    Common configurations
    """

    DEBUG = False


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEVELOPMENT = True
    DEBUG = True


    SQLALCHEMY_ECHO = False

    SERVER_NAME = 'localhost:5000'


app_config = {
    'development': DevelopmentConfig,

}
