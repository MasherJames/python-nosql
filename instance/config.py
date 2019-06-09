import os


class Config():
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    DATABASE_URL = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


app_config = {
    'development': DevelopmentConfig
}