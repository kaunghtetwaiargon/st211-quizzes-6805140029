from solution_bank import BankAccount

def test_deposit_independent ():
    account = BankAccount(1000)
    account.deposit(500)
    assert account.balance == 1500

def test_withdraw_independent ():
    account = BankAccount(1000)
    account.withdraw(300)
    assert account.balance == 700