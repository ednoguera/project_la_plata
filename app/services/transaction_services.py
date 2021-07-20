from app.models.models import Transaction

def serialize_transaction_list(transaction_list: Transaction) -> list:
    
    return [
        {
            'transaction_id': trans.transaction_id,
            'transaction_name': trans.transaction_name,
            'transaction_price': trans.transaction_price,
            'transaction_type': trans.transaction_type,
            'transaction_date': trans.transaction_date
        } for trans in transaction_list
    ]