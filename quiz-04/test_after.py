import pytest
from bank import BankAccount


@pytest.fixture
def account():
    return BankAccount(100)


def test_deposit(account):
    account.deposit(50)
    assert account.balance == 150


def test_withdraw(account):
    account.withdraw(30)
    assert account.balance == 70


def test_account_starts_with_fresh_balance(account):
    assert account.balance == 100


def test_insufficient_funds(account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(200)

    assert account.balance == 100
