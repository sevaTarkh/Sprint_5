import random
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Constants
from locators import Locators

class TestLoginUser:

    '''Login пользователя'''
    def test_login_user(self, driver):
        driver.get(Constants.url_doska)
        driver.find_element(*Locators.login_and_register_button).click()
        driver.find_element(*Locators.no_accaunt_button).click()

        email = f'user_{random.randint(0, 9999)}@mail.ru'
        password = '12345678'

        driver.find_element(*Locators.email_input).send_keys(email)
        driver.find_element(*Locators.password_input).send_keys(password)
        driver.find_element(*Locators.confirm_password_input).send_keys(password)

        driver.find_element(*Locators.create_accaunt_button).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.logout_button)
        )

        driver.find_element(*Locators.logout_button).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.login_and_register_button)
        )
        driver.find_element(*Locators.login_and_register_button).click()

        driver.find_element(*Locators.email_input).send_keys(email)
        driver.find_element(*Locators.password_input).send_keys(password)

        driver.find_element(*Locators.login_button).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.user_name)
        )
        assert (driver.find_element(*Locators.user_name) and
                driver.find_element(*Locators.logo))

    '''Logout пользователя'''
    def test_logout_user(self, driver):
        driver.get(Constants.url_doska)
        driver.find_element(*Locators.login_and_register_button).click()
        driver.find_element(*Locators.no_accaunt_button).click()

        email = f'user_{random.randint(0, 9999)}@mail.ru'
        password = '12345678'

        driver.find_element(*Locators.email_input).send_keys(email)
        driver.find_element(*Locators.password_input).send_keys(password)
        driver.find_element(*Locators.confirm_password_input).send_keys(password)

        driver.find_element(*Locators.create_accaunt_button).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.logout_button)
        )

        driver.find_element(*Locators.logout_button).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.login_and_register_button)
        )
        assert driver.find_element(*Locators.login_and_register_button)