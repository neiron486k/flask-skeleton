from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy(session_options=dict(autoflush=False, autocommit=False))
db = SQLAlchemy()


def orm_feature(app):
    """ Enables SQLAlchemy integration feature for database connectivity """
    db.init_app(app)
