from bson.objectid import ObjectId
import logging

def create_task(db, lead_id, task_data):
    task_data['lead_id'] = lead_id
    db.tasks.insert_one(task_data)

def get_all_tasks(db, lead_id):
    return db.tasks.find({"lead_id": lead_id})

def get_task(db, lead_id, task_id):
    return db.tasks.find_one({"lead_id": lead_id, "_id": ObjectId(task_id)})

def update_task(db, lead_id, task_id, update_data):
    logging.info(f"Updating task with lead_id: {lead_id}, task_id: {task_id}, update_data: {update_data}")
    if '_id' in update_data:
        del update_data['_id']
    result = db.tasks.update_one({"lead_id": lead_id, "_id": ObjectId(task_id)}, {"$set": update_data})
    logging.info(f"Update result: {result.modified_count} document(s) modified")

def delete_task(db, lead_id, task_id):
    db.tasks.delete_one({"lead_id": lead_id, "_id": ObjectId(task_id)})