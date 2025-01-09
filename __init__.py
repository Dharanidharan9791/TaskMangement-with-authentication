from flask import Flask
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from app.config import Config

mongo = PyMongo()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)  # Initialize MongoDB
    jwt.init_app(app)    # Initialize JWT

    # Import and register blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.lead_routes import lead_bp
    from app.routes.task_routes import task_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(lead_bp, url_prefix='/lead')
    app.register_blueprint(task_bp, url_prefix='/task')

    return app

app = create_app()
