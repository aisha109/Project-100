class atm(object):
    def __init__(self,users,atmNumber,atmPin):
        self.users = users
        self.atmNumber = atmNumber
        self.atmPin = atmPin

    def WithdrawMoney(self):
        print("Money has been withdrawed")

    def TransferMoney(self):
        print("Money has been transfered")

    def DepositMoney(self):
        print("Money has been deposited")

user1 = atm(1,12345,1122)
user2 = atm(2,56789,3344)
user3 = atm(3,13579,4455)


print(user1.TransferMoney())
print(user2.DepositMoney())
print(user3.WithdrawMoney())
