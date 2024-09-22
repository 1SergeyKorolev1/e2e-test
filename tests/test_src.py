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

def test_checkout(driver):
    checkout_button, func = src.checkout(driver, src.by)
    assert checkout_button

def test_giv_submission_form(driver):
    (
        first_name_input,
        last_name_input,
        postal_code,
        continue_button,
        func
    ) = src.giv_submission_form(driver, src.by)
    assert first_name_input
    assert last_name_input
    assert postal_code
    assert continue_button

def test_check_info_payment(driver):
    info_payment = src.check_info_payment(driver, src.by)
    assert info_payment

def test_finish(driver):
    finish_, func = src.finish(driver, src.by)
    assert finish_

def test_back_to(driver):
    back_to_btn, func = src.back_to(driver, src.by)
    assert back_to_btn