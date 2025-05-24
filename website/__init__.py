from flask import Flask
from flask_socketio import SocketIO
from . import config
from flask_login import LoginManager
from .models import db, User
from .utils import create_admin_user, create_roles
from sqlalchemy.exc import OperationalError
import time

socketio = SocketIO(cors_allowed_origins="*")

def create_monsys():
    app = Flask(__name__)

    # Load config settings
    app.config.from_object(config)

    db.init_app(app)

    login_manager = LoginManager(app)
    login_manager.login_view = 'auth.auth_login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    # Import and register blueprints
    from .auth import auth
    from .admin import admin
    from .api import api

    app.register_blueprint(auth)
    app.register_blueprint(admin)
    app.register_blueprint(api)

    # Retry loop for database connection
    max_retries = 5
    for attempt in range(max_retries):
        try:
            with app.app_context():
                # Initialize database tables
                db.create_all()
                # Ensure roles are created after the tables are ready
                create_roles()
                # Ensure admin user is created after the roles are ready
                create_admin_user()
            print("Database initialized successfully.")
            break
        except OperationalError as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"Database connection failed. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print("Failed to connect to the database after multiple attempts.")
                raise e  # Re-raise exception after max attempts
    
    socketio.init_app(app)
    return app