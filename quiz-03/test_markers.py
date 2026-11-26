import time

import pytest


@pytest.mark.smoke
def test_critical_login():
    assert True


@pytest.mark.smoke
def test_critical_checkout():
    assert True


@pytest.mark.slow
def test_full_report_generation():
    time.sleep(0.1)

    report = {
        "status": "complete",
        "records": 1000,
    }

    assert report["status"] == "complete"
    assert report["records"] == 1000


@pytest.mark.regression
def test_old_bug_stays_fixed():
    cart_total = 20 + 5

    assert cart_total == 25


@pytest.mark.regression
def test_empty_collection_regression():
    items = []

    assert len(items) == 0