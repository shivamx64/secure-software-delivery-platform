import os


class BaseConfig:
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


def get_config():
    env = os.getenv("SSDP_ENV", "development")

    if env == "production":
        return ProductionConfig
    return DevelopmentConfig