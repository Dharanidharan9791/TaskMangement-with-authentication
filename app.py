from flask import Flask
from flask_jwt_extended import JWTManager
from pymongo import MongoClient

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key

jwt = JWTManager(app)

# MongoDB connection
client = MongoClient("your_mongodb_connection_string")
db = client['task_manager']

if __name__ == "__main__":
    app.run(debug=True)
