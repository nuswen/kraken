from app import db

class messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text)
    amount = db.Column(db.Integer)

class product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text)
    amount = db.Column(db.Integer)

class creprod(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text)
    amount = db.Column(db.Integer)

class time(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Time = db.Column(db.Integer)