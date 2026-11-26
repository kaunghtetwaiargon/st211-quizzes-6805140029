from pytest import approx


def test_float_precision():
    assert 0.1 + 0.2 == approx(0.3)


def test_float_with_decimal():
    assert 1.5 + 2.5 == approx(4.0)


def test_float_multiplication():
    assert 0.1 * 3 == approx(0.3)


def test_float_list():
    result = [0.1 + 0.2, 0.2 + 0.2]

    assert result == approx([0.3, 0.4])


def test_float_with_absolute_tolerance():
    assert 10.001 == approx(10.0, abs=0.01)