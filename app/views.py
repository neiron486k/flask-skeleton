from app.bootstrap import app
from app.services.user_service import UserService
from flask import jsonify
from app.models.user import User

@app.route('/')
@app.route('/index')
def index():
    userService = UserService()
    data = {
        'nickname': 'neiron',
        'email': 'efsneiron@gmail.com'
    }
    user = userService.create(data)

    return jsonify(user.to_array())

@app.route('/user')
def user():
    user = User.query.get(1)

    return jsonify(user.to_array())