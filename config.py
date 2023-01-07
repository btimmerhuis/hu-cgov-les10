import os


# Determine the folder of the top-level directory of this project
BASEDIR = os.path.abspath(os.path.dirname(__file__))
DBPASS = os.getenv('DBPASS')


class Config(object):
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    # Logging
    LOG_WITH_GUNICORN = os.getenv('LOG_WITH_GUNICORN', default=False)
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://hules10:{DBPASS}@hu-lesson10.postgres.database.azure.com/todo?sslmode=require" # noqa
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    FLASK_ENV = 'production'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASEDIR, 'test.db')}"
    WTF_CSRF_ENABLED = False
