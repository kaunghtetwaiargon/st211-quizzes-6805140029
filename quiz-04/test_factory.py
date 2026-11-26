import pytest
from bank import BankAccount


@pytest.fixture
def make_account():
    def _make(balance):
        return BankAccount(balance)

    return _make


def test_small_account(make_account):
    account = make_account(100)
    assert account.balance == 100


def test_large_account(make_account):
    account = make_account(5000)
    assert account.balance == 5000


def test_multiple_accounts(make_account):
    account_a = make_account(100)
    account_b = make_account(200)

    assert account_a.balance == 100
    assert account_b.balance == 200


def test_accounts_are_independent(make_account):
    account_a = make_account(100)
    account_b = make_account(200)

    account_a.deposit(50)

    assert account_a.balance == 150
    assert account_b.balance == 200
