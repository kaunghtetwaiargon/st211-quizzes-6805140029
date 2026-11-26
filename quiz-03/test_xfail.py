import pytest


@pytest.mark.xfail(
    reason="Known bug; fix pending",
    strict=True,
)
def test_known_broken_feature():
    assert 1 == 2


def test_working_feature():
    assert 1 == 1