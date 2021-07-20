from sqlalchemy import and_
from flask import (
    Blueprint,
    request
)
from http import HTTPStatus
from app.models.models import (
    Transaction,
    db
)

from sqlalchemy.exc import IntegrityError

# SERIEALIZERS
from app.services.transaction_services import serialize_transaction_list
from app.services.monthly_statement_service import serialize_monthly_statements

# CREATE MONTHLY STATEMENT BLUEPRINT
bp_monthly_statements = Blueprint('bp_monthly_statements', __name__, url_prefix='/users/<int:user_id>')


@bp_monthly_statements.route('/monthly-statements/<transaction_month>', methods=["GET"])
def get_monthly_statements_by_user(user_id: int, transaction_month: str) -> dict:
    transaction_map = Transaction.query.filter(
        Transaction.user_id == user_id,
        Transaction.transaction_month == transaction_month
    )
    transactions_by_month = serialize_transaction_list(transaction_map)
    
    print(transactions_by_month)
    
    return {
        "Statements Ref": 
            transactions_by_month
        
    }