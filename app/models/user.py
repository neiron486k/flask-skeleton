from bucket.feature.orm import db
from .common import Entity


class User(Entity, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    items = db.relationship('Item', backref='user',
                            lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.nickname)

    def to_array(self):
        return {
            'id': self.id,
            'nickname': self.nickname,
            'email': self.email
        }


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<User %r>' % (self.title)
