from flask import Blueprint, request
from http import HTTPStatus

# IMPORT DB AND DOMAIN CLASS FROM MODELS
from app.models.models import db, User, Transaction

bp_transactions = Blueprint('bp_transaction', __name__, url_prefix='/transactions')

def serialize_list(gen_list) -> list:
    return [{
            'transaction_id': gen.transaction_id,
            'transaction_name': gen.transaction_name,
            'transaction_price': gen.transaction_price,
            'transaction_type': gen.transaction_type
        } 
        for gen in gen_list
    ]

@bp_transactions.route('/', methods=["GET", "POST"])
def set_transaction() -> dict:
    
    # IF METHOD EQUALS POST
    if request.method == "POST":
        transaction = Transaction(
            transaction_name=request.json["transaction_name"],
            transaction_price=request.json["transaction_price"],
            transaction_type=request.json["transaction_type"]
        )
        
        db.session.add(transaction)
        db.session.commit()
    
        return {
            'request_status': HTTPStatus.CREATED
        }
    
    # IF METHOD EQUALS GET    
    transaction_list = Transaction.query.all()
    transaction_dict = serialize_list(transaction_list)
    
    return {
        'transactions': transaction_dict
    }