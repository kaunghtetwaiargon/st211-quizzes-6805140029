import pytest

from shopping import ShoppingCart


class TestShoppingCart:

    def test_new_cart_is_empty(self):
        cart = ShoppingCart()

        assert cart.count() == 0

    def test_new_cart_total_is_zero(self):
        cart = ShoppingCart()

        assert cart.total() == 0

    def test_add_item_increases_count(self):
        cart = ShoppingCart()

        cart.add("Book", 20)

        assert cart.count() == 1

    def test_total_sums_prices(self):
        cart = ShoppingCart()

        cart.add("Book", 20)
        cart.add("Pen", 5)

        assert cart.total() == 25

    def test_add_multiple_items(self):
        cart = ShoppingCart()

        cart.add("Book", 20)
        cart.add("Pen", 5)
        cart.add("Notebook", 10)

        assert cart.count() == 3

    def test_total_after_adding_multiple_items(self):
        cart = ShoppingCart()

        cart.add("Book", 20)
        cart.add("Pen", 5)
        cart.add("Notebook", 10)

        assert cart.total() == 35

    def test_item_name_is_saved(self):
        cart = ShoppingCart()

        cart.add("Book", 20)

        assert cart.items[0]["name"] == "Book"

    def test_item_price_is_saved(self):
        cart = ShoppingCart()

        cart.add("Book", 20)

        assert cart.items[0]["price"] == 20

    def test_adding_zero_price_item(self):
        cart = ShoppingCart()

        cart.add("Free Book", 0)

        assert cart.total() == 0

    @pytest.mark.regression
    def test_total_regression(self):
        cart = ShoppingCart()

        cart.add("Book", 20)
        cart.add("Pen", 5)

        assert cart.total() == 25

    @pytest.mark.smoke
    def test_cart_can_add_item(self):
        cart = ShoppingCart()

        cart.add("Book", 20)

        assert cart.count() == 1