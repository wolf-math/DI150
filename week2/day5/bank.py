class BankAccount:
    def __init__(self, account_number, balance=0, minimum_balance=0):
        self.account_number = account_number
        self.balance = balance
        self.minimum_balance = minimum_balance


    def view_balance(self):
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            self.balance += amount
            print("Deposit Succcessful")

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            raise Exception("The withdraw amount is too much")
        else:
            self.balance -= amount



ryan = BankAccount(10, 9_000_000)
aaron = BankAccount(11, 150)

ryan.withdraw(1_000_000)

ryan.view_balance()
