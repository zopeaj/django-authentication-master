class AuthManager:
    def __init__(self):
        self.authenticated = False

    def removeAuthentication(self, username):
        if username is not None:
            return self.authenticated

    def setAuthentication(self, username, password):
        return self.authenticate(username, password)

    def authenticate(self, username, password):
        if username and password is not None:
            self.authenticated = True
        return False

authManager = AuthManager()
