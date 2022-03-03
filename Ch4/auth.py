from unicodedata import name


class User:
    def __init__(self, name, init_password):
        self.name = name
        self.password = self._get_password(init_password)
        self.is_logged_in = False

    def _get_password(self, init_password):
        return init_password + "XXXX"
    
    def check_password(self, input_password):
        return self._get_password(input_password) == self.password


class Authenticator:
    users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UserAlreadyExists(username)
        if len(password) < 3:
            raise PasswordTooShort
        self.users[username] = User(username, password)
    
    def login(self, user_name, input_password):
        try:
            user = self.users[user_name]
        except KeyError:
            raise UserDoesNotExist
        else:
            if user.check_password(input_password):
                user.is_logged_in = True
            else:
                raise WrongPassword
    
    def is_logged_in(self, username):
        try:
            user = self.users[username]
        except KeyError:
            raise UserDoesNotExist
        else:
            return user.is_logged_in

class AuthException(Exception):
    def __init__(self, username=None, user=None):
        super().__init__(username, user)
        self.username = username
        self.user = user

class UserAlreadyExists(AuthException):
    pass

class PasswordTooShort(AuthException):
    pass

class UserDoesNotExist(AuthException):
    pass

class WrongPassword(AuthException):
    pass

class Authorizor:
    pass