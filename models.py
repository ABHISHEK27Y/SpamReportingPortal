from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    profile_pic = db.Column(db.String(200))

class Complaint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message_content = db.Column(db.Text, nullable=False)
    is_spam_prediction = db.Column(db.Integer, nullable=False) # 1 for spam, 0 for legit
    probabilities = db.Column(db.String(50)) # Store as string "fraud_prob,legit_prob"
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
