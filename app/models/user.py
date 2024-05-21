from app import mongo, bcrypt


class User:
    def __init__(self, username, email, password, favorites=None):
        self.username = username
        self.email = email
        self.password = password
        self.favorites = favorites if favorites else []

    def register(self):
        try:
            users = mongo.db.users
            if users is None:
                return False, 'Error occur try again later'
            existing_user = users.find_one({'email': self.email}) if users is not None else None
            if existing_user is None:
                hashpass = bcrypt.generate_password_hash(self.password).decode('utf-8')
                result = users.insert_one({'username': self.username, 'email': self.email, 'password': hashpass})
                user_id = result.inserted_id
                return True, str(user_id)
            return False, str(existing_user['_id']) if existing_user else 'Error occur try again later'
        except Exception as e:
            print(e)
            return False, 'Error occur try again later'


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
