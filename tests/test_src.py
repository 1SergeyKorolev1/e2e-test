import src
import pytest

@pytest.fixture
def driver():
    driver = src.driver
    return driver

def test_give_authorization(driver):
    user_name, password_input, login_button_, func = src.give_authorization(driver, src.by, src)
    assert user_name
    assert password_input
    assert login_button_

def test_added_to_cart(driver):
    labs_backpack_product, func = src.added_to_cart(driver, src.by)
    assert labs_backpack_product

def test_go_to_cart(driver):
    shopping_cart_link, func = src.go_to_cart(driver, src.by)
    assert shopping_cart_link

def test_check_product_in_cart(driver):
    product_in_cart = src.check_product_in_cart(driver, src.by)
    assert product_in_cart