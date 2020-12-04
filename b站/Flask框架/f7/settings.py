class BaseConfig(object):
    DEBUG=True
    TESTING=False
    SECRET_KEY="asdfsefgsafa"
    DATABASE_URI="sqlite://:memory"

class ProductionConfig(BaseConfig):
    '''
    正式环境
    '''
    DEBUG = False
    DATABASE_URL='mysql://user@pro/foo'

class DevelopmentConfig(BaseConfig):
    '''
    开发环境
    '''
    DATABASE_URL='mysql://user@dev/foo'

class TestingConfig(BaseConfig):
    '''
    测试环境
    '''
    DATABASE_URL='mysql://user@test/foo'