import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-fallback-change-in-production'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///placement.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads', 'resumes')


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}