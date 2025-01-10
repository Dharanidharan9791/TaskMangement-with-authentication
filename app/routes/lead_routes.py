from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.database import db
from app.models.lead_model import create_lead

lead_bp = Blueprint('lead', __name__)

@lead_bp.route('/', methods=['POST'])
@jwt_required()
def create_lead_route():
    data = request.json
    company_id = request.args.get('company_id')
    if not company_id:
        return jsonify({"error": "Company ID is required"}), 400

    # Pass db to the create_lead function
    create_lead(db, {
        "company": data['company'],
        "contact": data['contact'],
        "company_id": company_id
    })
    return jsonify({"message": "Lead created successfully"}), 201

@lead_bp.route('/allLeads', methods=['GET'])
@jwt_required()
def get_tasks():
    print("Type of lead_id:",list(db.leads.find({})))
    try:
        # Query the database
        leads = list(db.leads.find({}))

        # Convert ObjectId to string
        for lead in leads:
            lead['_id'] = str(lead['_id'])

        return jsonify( leads), 200
    except Exception as e:
        print("Error during query:", str(e))
        return jsonify({"error": "Failed to fetch tasks", "details": str(e)}), 500
