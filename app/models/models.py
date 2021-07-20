from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

db = SQLAlchemy()
mg = Migrate()   

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    transactions = db.relationship("Transaction", back_populates="user")


    def __repr__(self) -> str:
        return '<User {}, Email {}>'.format(self.username, self.email)
    


class Transaction(db.Model):
    __tablename__ = "transaction"
    transaction_id = db.Column(
        db.Integer, 
        nullable=False, 
        autoincrement=True, 
        primary_key=True
    )
    transaction_name = db.Column(
        db.String(100),
        nullable=False
    )
    transaction_price = db.Column(
        db.Float,
        nullable=False
    )
    transaction_type = db.Column(
        db.String(3), 
        nullable=False
    )
    transaction_month = db.Column(
        db.String(3),
        nullable=False,
        default="JAN"
    )
    transaction_timestamp = db.Column(
        db.DateTime(),
        nullable=False,
        default=datetime.utcnow
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id')
    )
    user = db.relationship(
        "User",
        back_populates="transactions"
    )
    
    def __repr__(self) -> str:
        return f"Transaction id: {self.transaction_id}"

