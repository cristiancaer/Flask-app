from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

from app.models.users import UserModel
from .config import Config
from .auth import auth


login_manager=LoginManager()
login_manager.login_view='auth.login'

@login_manager.user_loader
def load_user(user_id):
    return  UserModel.query(user_id)

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    bootstrap=Bootstrap(app)
    login_manager.init_app(app)
    app.register_blueprint(auth)
    
    return app