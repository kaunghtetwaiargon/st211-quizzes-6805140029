import pytest
from discount import apply_discount

@pytest.mark.parametrize("price, discount, expected", [
    pytest.param(100, 0, 100, id="no_discount"),
    pytest.param(100, 50, 50, id="half_off"),
    pytest.param(100, 100, 0, id="free"),
])
def test_apply_discount(price, discount, expected):
    assert apply_discount(price, discount) == expected