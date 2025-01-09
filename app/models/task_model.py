def create_task(db, lead_id, task_data):
    task_data['lead_id'] = lead_id
    db.tasks.insert_one(task_data)

def get_all_tasks(db, lead_id):
    return list(db.tasks.find({"lead_id": lead_id}))

def get_task(db, lead_id, task_id):
    return db.tasks.find_one({"lead_id": lead_id, "_id": task_id})

def update_task(db, lead_id, task_id, update_data):
    db.tasks.update_one({"lead_id": lead_id, "_id": task_id}, {"$set": update_data})

def delete_task(db, lead_id, task_id):
    db.tasks.delete_one({"lead_id": lead_id, "_id": task_id})
