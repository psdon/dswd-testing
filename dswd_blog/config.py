import os


class BaseConfig:
    ENV = os.environ.get("FLASK_ENV", "production")
    DEBUG = ENV == "development"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    PASSWORD_SALT_KEY = os.environ.get("PASSWORD_SALT_KEY")


class DevConfig(BaseConfig):
    # mail settings
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    # gmail authentication
    MAIL_USERNAME = "dswd.testing@gmail.com"
    MAIL_PASSWORD = "^aFqbr8&hQ0x"

    # mail accounts
    MAIL_DEFAULT_SENDER = "dswd.testing@gmail.com"


class TestingConfig(BaseConfig):
    TESTING = True
