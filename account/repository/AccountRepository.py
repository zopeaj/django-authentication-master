from account.models import Account

class AccountRepository:
    def __init__(self, account):
        self.account = account

    def save(self, account_data):
        self.account.objects.create(account_data)
        self.account.save()

    def update(self, account_data, account_id):
        account = self.account.get(id=account_id)
        account.update(account_data)
        return account

    def delete(self, account_id):
        self.account.get(id=account_id)
        self.account.delete()


accountRepository = AccountRepository(Account())

