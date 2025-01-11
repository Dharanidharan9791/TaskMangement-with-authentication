from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models.task_model import create_task, get_all_tasks, get_task, update_task, delete_task
from app.database import db
from bson.objectid import ObjectId

task_bp = Blueprint('task', __name__)

@task_bp.route('/addTask', methods=['POST'])
@jwt_required()
def create_task_route():
    data = request.json
    company_id = request.args.get('company_id')
    if not company_id:
        return jsonify({"error": "Company ID is required"}), 400

    create_task(db, company_id, data)
    return jsonify({"message": "Task created successfully"}), 201



@task_bp.route('/<lead_id>', methods=['GET'])
@jwt_required()
def get_tasks(lead_id):
    try:
        lead_id = lead_id.strip('"').strip("'")
        print("Received lead_id:", lead_id) 
        tasks = list(db.tasks.find({"lead_id": lead_id}))
        print("Fetched tasks:", tasks)  
        for task in tasks:
            task['_id'] = str(task['_id'])
        return jsonify(tasks), 200
    except Exception as e:
        print("Error during query:", str(e))
        return jsonify({"error": "Failed to fetch tasks", "details": str(e)}), 500
    
@task_bp.route('/<lead_id>/<task_id>', methods=['GET'])
@jwt_required()
def get_task_route(lead_id, task_id):
    task = get_task(db, lead_id, task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task), 200



@task_bp.route('/<lead_id>/<task_id>', methods=['PUT'])
@jwt_required()
def update_task_route(lead_id, task_id):
    lead_id = lead_id.strip('"').strip("'")
    task_id = task_id.strip('"').strip("'")
    data = request.json
    update_task(db, lead_id, task_id, data)
    return jsonify({"message": "Task updated successfully"}), 200

@task_bp.route('/<lead_id>/<task_id>', methods=['DELETE'])
@jwt_required()
def delete_task_route(lead_id, task_id):
    lead_id = lead_id.strip('"').strip("'")
    task_id = task_id.strip('"').strip("'")
    delete_task(db, lead_id, task_id)
    return jsonify({"message": "Task deleted successfully"}), 200