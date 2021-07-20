import enum
from flask import Blueprint, request
from http import HTTPStatus


# IMPORT DB AND DOMAIN CLASS FROM MODELS
from app.models.models import db, Transaction


# IMPORT TRANSACTION SERVICE
from app.services.transaction_services import serialize_transaction_list

bp_transactions = Blueprint('bp_transaction', __name__, url_prefix='/users/<int:user_id>')
        

@bp_transactions.route('/transactions', methods=["POST"])
def set_transaction(user_id: int) -> dict:
    
    transaction = Transaction(
        transaction_name=request.json["transaction_name"],
        transaction_price=request.json["transaction_price"],
        transaction_type=request.json["transaction_type"],
        user_id=user_id
    )
    
    db.session.add(transaction)
    db.session.commit()

    return {
        'request_status': HTTPStatus.CREATED
    }
    

@bp_transactions.route('/transactions', methods=["GET"])
def get_transactions(user_id: int):
    transaction_map = Transaction.query.filter(Transaction.user_id == user_id)
    transaction_by_user = serialize_transaction_list(transaction_map)
    
    if not transaction_by_user:
        return "Transaction not exists"
    print(transaction_by_user)
    
    return {'transaction': transaction_by_user}