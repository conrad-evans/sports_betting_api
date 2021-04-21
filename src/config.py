class Config(object):
    """
    base app configurations
    """
    TESTING = False
    DEBUG = False


class ProductionConfig(Config):
    """
    app configuration for production environment
    """
    pass


class DevelopmentConfig(Config):
    """
    app configuration for development environment
    """
    TESTING = False
    DEBUG = True


class TestingConfig(Config):
    """
    app configuration for testing environment
    """
    TESTING = True
    DEBUG = True
