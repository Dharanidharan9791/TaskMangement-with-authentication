from flask_jwt_extended import get_jwt_identity

def get_current_user_id():
    """Retrieve the user ID from the JWT token."""
    return get_jwt_identity()
