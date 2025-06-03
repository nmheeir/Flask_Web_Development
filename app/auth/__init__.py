from flask import Blueprint, request
from flask_login import current_user, user_logged_in, user_logged_out
from app.models import UserLog, db
from app import db

auth = Blueprint('auth', __name__)

from . import views

@user_logged_in.connect
def log_user_login(sender, user):
    log = UserLog(user_id=user.id, action='login', ip=request.remote_addr)
    db.session.add(log)
    db.session.commit()

@user_logged_out.connect
def log_user_logout(sender, user):
    log = UserLog(user_id=user.id, action='logout', ip=request.remote_addr)
    db.session.add(log)
    db.session.commit()