from app.models.models import User

def serialize_user(user: User) -> dict:
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email
    }

def serialize_user_list(gen_list) -> list:
    return [{'id': gen.id, 'name': gen.username, 'email': gen.email} for gen in gen_list]
    