def create_lead(db, lead_data):
    db.leads.insert_one(lead_data)
