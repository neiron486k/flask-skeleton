from bucket.config.default_settings import DefaultConfig
import os


class DevConfig(DefaultConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/flask'
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    OPENID_PROVIDERS = [
        {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
        {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
        {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
        {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
        {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]
