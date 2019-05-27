from app import db

class messages(db.Model):
    url = db.Column(db.Text)