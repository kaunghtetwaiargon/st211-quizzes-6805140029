class BankAccount:

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

BankAccount1 = BankAccount(1000)
withdrawn_amount = BankAccount1.withdraw(650)


print(f"Remaining Balance: {BankAccount1.balance}")