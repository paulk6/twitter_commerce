from app import app, db
from datetime import datetime



class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.String(140))
    date_posted = db.Column(db.DateTime, default=datetime.now().date())

class Contact(db.Model):
    contact_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    email = db.Column(db.String(50))
    message = db.Column(db.String(300))
    date_posted = db.Column(db.DateTime, default=datetime.now().date())
