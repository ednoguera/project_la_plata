from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    Id = db.Column(db.Integer, nullable=False, primary_key=True)
    Username = db.Column(db.String(50), unique=True, nullable=False)
    Email = db.Column(db.String(100), unique=True, nullable=False)


    def __repr__(self) -> str:
        return '<User %r>' % self.Username

