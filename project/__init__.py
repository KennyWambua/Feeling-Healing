from flask import Flask
import secrets
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate



# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = secrets.token_hex(16)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)
    migrate.init_app(app, db)
    
    from project import models
    from .models import User
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    # def initialize_database():
    #     db.create_all()
        
    #     if not models.User.query.first():
    #         admin_user = models.User(name='Admin', email="kenedywambuah@gmail.com", password="Kennedy@123", role="staff")
    #         db.session.add(admin_user)
            
    #     if not models.Service.query.first():
    #         service_ex = models.Service(name="Yoga", description="Yoga Classes...")
    #         db.session.add(service_ex)
            
    #     db.session.commit()

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app 
# initialize_database()