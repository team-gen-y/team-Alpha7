from flaskapp import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class cardioData(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Integer,nullable=False)
    systolic = db.Column(db.Integer, nullable=False)
    diastolic = db.Column(db.Integer, nullable=False)
    cholestrol = db.Column(db.Integer, nullable=False)
    glucose = db.Column(db.Integer, nullable=False)
    alcohol = db.Column(db.Integer)
    physical = db.Column(db.Integer)
    smoking = db.Column(db.Integer)
    disease = db.Column(db.Integer)

    def __repr__(self):
        return f"User('{self.name}','{self.height}','{self.age}','{self.weight}','{self.gender}','{self.cholestrol}','{self.glucose}','{self.alcohol}')"

class cardioDataLogged(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Integer,nullable=False)
    systolic = db.Column(db.Integer, nullable=False)
    diastolic = db.Column(db.Integer, nullable=False)
    cholestrol = db.Column(db.Integer, nullable=False)
    glucose = db.Column(db.Integer, nullable=False)
    alcohol = db.Column(db.Integer)
    physical = db.Column(db.Integer)
    smoking = db.Column(db.Integer)
    disease = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    def __repr__(self):
        return f"User('{self.name}', '{self.user_id}')"

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    cardiodata = db.relationship('cardioDataLogged',backref="user",lazy=True)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


   