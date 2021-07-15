from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)


    def __repr__(self) -> str:
        return '<User {}, Email {}>'.format(self.username, self.email)

