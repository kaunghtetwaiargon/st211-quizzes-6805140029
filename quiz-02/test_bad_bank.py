from solution_bank import BankAccount

def test_deposit_increase_balance ():
    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(100)
    account.deposit(100)
    assert account.balance == 150