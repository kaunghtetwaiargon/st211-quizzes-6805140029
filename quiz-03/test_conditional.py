import os

import pytest


@pytest.mark.skipif(
    not os.path.exists("/etc/hosts"),
    reason="Hosts file does not exist",
)
def test_hosts_file():
    assert os.path.exists("/etc/hosts")


def test_current_directory_exists():
    assert os.path.isdir(".")