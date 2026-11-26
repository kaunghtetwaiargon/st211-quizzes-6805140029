from solution_bank import BankAccount

shared_account = BankAccount(100)

def test_a_deposit():
    shared_account.deposit(150)
    assert shared_account.balance == 250

def test_b_withdraw():
    shared_account.withdraw(30)
    assert shared_account.balance == 220