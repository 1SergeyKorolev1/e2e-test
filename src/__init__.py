from selenium import webdriver
from src.give_authorization import give_authorization
from src.added_to_cart import added_to_cart
from src.submission_form import giv_submission_form
from src.finish_and_back_to import finish_and_back_to

driver = webdriver.Chrome()

start_dict = {
    "link": "https://www.saucedemo.com/",
    "user_name": "standard_user",
    "password": "secret_sauce"
}
