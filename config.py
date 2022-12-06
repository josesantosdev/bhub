from instance import config

class DevelopmentConfig(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{config.local_user}:{config.local_password}@{config.local_host}/{config.local_db}'
    DATABASE_CONNECT_OPTIONS = {}
   