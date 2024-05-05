from CellPhone.models import User
from CellPhone import app, db
import hashlib
from flask_login import current_user
from sqlalchemy import func
import cloudinary.uploader

def get_user_by_id(user_id):
    return User.query.get(user_id)
