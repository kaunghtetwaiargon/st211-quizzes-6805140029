def test_empty_account_starts_at_zero(empty_account):
    assert empty_account.balance == 0


def test_funded_account_has_money(funded_account):
    assert funded_account.balance == 1000


def test_empty_account_can_receive_deposit(empty_account):
    empty_account.deposit(100)
    assert empty_account.balance == 100
