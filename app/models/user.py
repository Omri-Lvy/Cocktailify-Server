from app import mongo, bcrypt


class User:
    def __init__(self, username, email, password, favorites=None):
        self.username = username
        self.email = email
        self.password = password
        self.favorites = favorites if favorites else []

    def register(self):
        users = mongo.db.users
        if users is None:
            return False, 'Error occur try again later'
        existing_user = users.find_one({'username': self.username}) if users is not None else None
        if existing_user is None:
            hashpass = bcrypt.generate_password_hash(self.password).decode('utf-8')
            users.insert_one({'username': self.username, 'email': self.email, 'password': hashpass})
            return True, ''
        return False, 'User exists'

    @staticmethod
    def login(username, password):
        users = mongo.db.users
        login_user = users.find_one({
            '$or': [
                {'username': username},
                {'email': username}
            ]
        })
        if login_user:
            if bcrypt.check_password_hash(login_user['password'], password):
                return True
        return False
