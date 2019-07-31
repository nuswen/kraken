from app import db

class messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text)

class Product(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Url = db.Column(db.Text)
    Amount = db.Column(db.Integer)