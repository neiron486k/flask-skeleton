from bucket import bootstrap

app = bootstrap.create_app(__name__, 'app.config.default_settings.DevConfig')
bootstrap.add_orm(app)
bootstrap.add_debug_toolbar(app)

from app.models.user import User
from app import views