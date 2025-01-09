from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models.task_model import create_task, get_all_tasks, get_task, update_task, delete_task
from app import mongo  # Import mongo

task_bp = Blueprint('task', __name__)

@task_bp.route('/<lead_id>', methods=['POST'])
@jwt_required()
def create_task_route(lead_id):
    data = request.json
    company_id = request.args.get('company_id')
    if not company_id:
        return jsonify({"error": "Company ID is required"}), 400

    create_task(mongo.db, lead_id, data)
    return jsonify({"message": "Task created successfully"}), 201

@task_bp.route('/<lead_id>', methods=['GET'])
@jwt_required()
def get_tasks(lead_id):
    tasks = get_all_tasks(mongo.db, lead_id)
    return jsonify(tasks), 200

@task_bp.route('/<lead_id>/<task_id>', methods=['GET'])
@jwt_required()
def get_task_route(lead_id, task_id):
    task = get_task(mongo.db, lead_id, task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task), 200

@task_bp.route('/<lead_id>/<task_id>', methods=['PUT'])
@jwt_required()
def update_task_route(lead_id, task_id):
    data = request.json
    update_task(mongo.db, lead_id, task_id, data)
    return jsonify({"message": "Task updated successfully"}), 200

@task_bp.route('/<lead_id>/<task_id>', methods=['DELETE'])
@jwt_required()
def delete_task_route(lead_id, task_id):
    delete_task(mongo.db, lead_id, task_id)
    return jsonify({"message": "Task deleted successfully"}), 200
