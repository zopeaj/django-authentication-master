from account.repository.AccountRepository import accountRepository

class AccountService:
    def __init__(self, accountRepository):
        self.accountRepository = accountRepository

    def save(self, data):
        self.accountRepository.save(data)

    def delete(self, id):
        self.accountRepository.delete(id)

    def update(self, id, data):
        return self.accountRepository.update(id, data)

    def getAccountById(self, id):
        return self.accountRepository.getById(id)

accountService = AccountService(accountRepository)

