from bucket.feature.orm import db
from app.models.user import User

class UserService:
    def create(self, data):
        user = User(data)
        db.session.add(user)
        db.session.commit()

        return user
