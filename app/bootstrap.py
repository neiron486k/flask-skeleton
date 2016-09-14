from bucket import bootstrap

app = bootstrap.create_app('app.config.default_settings.DevConfig')
bootstrap.add_orm(app)

from app.models.user import User
from app import views
