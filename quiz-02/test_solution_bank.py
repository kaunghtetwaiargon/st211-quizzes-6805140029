from solution_bank import BankAccount

def test_deposit_increase_balance ():
    account = BankAccount(100)
    account.deposit(50)
    assert account.balance == 150