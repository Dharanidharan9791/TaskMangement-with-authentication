from flask import Flask
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from flask_cors import CORS
from app.config import Config

mongo = PyMongo()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    mongo.init_app(app)  # Initialize MongoDB
    jwt.init_app(app)    # Initialize JWT

    # Enable CORS
    CORS(app)

    # Import and register blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.lead_routes import lead_bp
    from app.routes.task_routes import task_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(lead_bp, url_prefix='/lead')
    app.register_blueprint(task_bp, url_prefix='/task')

    @app.route('/')
    def home():
        return {"message": "CORS is enabled!"}

    return app

app = create_app()
