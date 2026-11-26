import sys

import pytest


@pytest.mark.skip(reason="Feature not implemented yet")
def test_future_feature():
    assert False


@pytest.mark.skipif(
    sys.version_info < (3, 8),
    reason="Requires Python 3.8 or newer",
)
def test_needs_modern_python():
    assert True


def test_normal_functionality():
    assert 2 + 2 == 4