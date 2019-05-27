from app import db

class messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text)