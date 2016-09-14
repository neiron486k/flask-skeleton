from flask import Flask


def create_app(config='bucket.config.default_settings.DevConfig'):
    """ Creates app """
    app = Flask(__name__)
    app.config.from_object(config)

    return app


def add_orm(app):
    """ Add SQLAlchemy ORM integration """
    from bucket.feature.orm import orm_feature
    orm_feature(app)
