from flask import Blueprint, request, jsonify
from app.database import db
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    users_collection = db.users  # Access the "users" collection
    existing_user = users_collection.find_one({"email": data["email"]})

    if existing_user:
        return jsonify({"message": "User already exists"}), 400

    users_collection.insert_one({
        "first_name": data["first_name"],
        "last_name": data["last_name"],
        "email": data["email"],
        "password": data["password"]  # In production, hash passwords!
    })

    return jsonify({"message": "Registration successful"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    users_collection = db.users
    user = users_collection.find_one({"email": data["email"]})

    if not user or user["password"] != data["password"]:  # Use hashed passwords in production
        return jsonify({"message": "Invalid credentials"}), 401

    access_token = create_access_token(identity=str(user["_id"]))
    return jsonify({"access_token": access_token}), 200
