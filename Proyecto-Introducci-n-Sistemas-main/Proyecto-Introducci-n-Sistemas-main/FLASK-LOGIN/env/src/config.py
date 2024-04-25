class Config:
    SECRET_KEY = 'Contraseña super secreta'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '123456'
    MYSQL_DB = 'FLASK-LOGIN' 



config = {
    'development':DevelopmentConfig
}
