from app.models.user import User

def handle_register(data):
    try:
        if not data:
            return {'isSuccess': False, 'message': 'No data provided'}, 400

        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not all([name, email, password]):
            return {'isSuccess': False, 'message': 'Missing required fields'}, 400

        user = User(name, email, password, [])
        isSuccess, user = user.register()

        message = 'User registered successfully' if isSuccess else 'User already exists'
        results = {
            'isSuccess': isSuccess,
            'message': message,
            'user': {
                'id': user['_id'],
                'favorites': user['favorites']
            } if user else None
        }
        return results, 200 if isSuccess else 400

    except RuntimeError:
        return {'isSuccess': False, 'message': 'Server Error occurred'}, 500


def handle_login(data):
    try:
        if not data:
            return {'isSuccess': False, 'message': 'No data provided'}, 400

        email = data.get('email')
        password = data.get('password')
        isSuccess, user = User.login(email, password)

        if user:
            results = {
                'isSuccess': isSuccess,
                'message': 'User logged in!' if isSuccess else 'Email or password is incorrect',
                'user': {
                    'id': str(user['_id']),
                    'favorites': user['favorites']
                }
            }
        else:
            results = {
                'isSuccess': isSuccess,
                'message': 'Email or password is incorrect',
                'user': None
            }
        return results, 200 if isSuccess else 400

    except RuntimeError:
        return {'isSuccess': False, 'message': 'Server Error occurred'}, 500