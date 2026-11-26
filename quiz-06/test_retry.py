from unittest.mock import Mock
from retry import charge_with_retry


def test_succeeds_after_retries():
    gateway = Mock()

    gateway.charge.side_effect = [
        ConnectionError("fail 1"),
        ConnectionError("fail 2"),
        "SUCCESS",
    ]

    assert charge_with_retry(gateway, 100) == "SUCCESS"
    assert gateway.charge.call_count == 3
