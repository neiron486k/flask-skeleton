from bucket import bootstrap
from flask_login import LoginManager
from flask_openid import OpenID
import os

app = bootstrap.create_app(__name__, 'app.config.default_settings.DevConfig')
bootstrap.add_orm(app)
bootstrap.add_debug_toolbar(app)
basedir = app.config['BASEDIR']
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views, models