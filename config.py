import os

class Config:
    '''
    General configuration parent class
    '''
    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ornella:kko@localhost/blog'
    SECRET_KEY='secret'
    # UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "ornellakankazi@gmail.com"
    MAIL_PASSWORD = "1234"
    

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
        
class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True    

config_options ={
    'development':DevConfig,
    'production':ProdConfig,
}