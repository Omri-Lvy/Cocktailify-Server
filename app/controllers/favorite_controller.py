from app.models.user import User


def handle_add_favorite(data):
    try:
        if not data:
            return {'isSuccess': False, 'message': 'No data provided'}, 400

        user_id = data.get('user_id')
        cocktail = data.get('cocktail')
        isSuccess, message = User.add_to_favorites(user_id, cocktail)

        return {'isSuccess': isSuccess, 'message': message}, 200 if isSuccess else 400

    except RuntimeError:
        return {'isSuccess': False, 'message': 'Server Error occurred'}, 500


def handle_remove_favorite(data):
    try:
        if not data:
            return {'isSuccess': False, 'message': 'No data provided'}, 400

        user_id = data.get('user_id')
        cocktail = data.get('cocktail_id')
        isSuccess, message = User.remove_from_favorites(user_id, cocktail)

        return {'isSuccess': isSuccess, 'message': message}, 200 if isSuccess else 400

    except RuntimeError:
        return {'isSuccess': False, 'message': 'Server Error occurred'}, 500