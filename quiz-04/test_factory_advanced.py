import pytest


@pytest.fixture
def make_user():
    created = []

    def _make(name, role="user"):
        user = {
            "name": name,
            "role": role,
            "active": True,
        }

        created.append(user)
        return user

    yield _make

    print(f"\n[cleanup] created {len(created)} users during test")


def test_default_role(make_user):
    user = make_user("Alice")

    assert user["name"] == "Alice"
    assert user["role"] == "user"
    assert user["active"] is True


def test_custom_role(make_user):
    user = make_user("Bob", role="admin")

    assert user["role"] == "admin"


def test_multiple_users(make_user):
    user_a = make_user("Alice")
    user_b = make_user("Bob", role="admin")

    assert user_a["name"] == "Alice"
    assert user_b["name"] == "Bob"
    assert user_a["role"] == "user"
    assert user_b["role"] == "admin"


def test_users_are_independent(make_user):
    user_a = make_user("Alice")
    user_b = make_user("Bob")

    user_a["active"] = False

    assert user_a["active"] is False
    assert user_b["active"] is True
