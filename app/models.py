from app import db

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text)