from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    transactions = db.relationship("Transaction", back_populates="user")


    def __repr__(self) -> str:
        return '<User {}, Email {}>'.format(self.username, self.email)
    


class Transaction(db.Model):
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
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id')
    )
    user = db.relationship(
        "User",
        back_populates="transactions"
    )
    
    def __repr__(self) -> str:
        return """{'transaction_id': {}, 
    'transaction_name': {}, 
    'transaction_cost': {} }""".format(
            self.transaction_id, 
            self.transaction_name, 
            self.transaction_cost            
        )

