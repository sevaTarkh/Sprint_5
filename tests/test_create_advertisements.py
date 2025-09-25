import random
import string
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Constants
from locators import Locators

class TestCreatingAdvertisements:

    '''Создание объявления неавторизованным пользователем'''
    def test_create_advertisements_unauthorized_user(self, driver):
        driver.get(Constants.url_doska)
        driver.find_element(*Locators.add_announcement).click()

        assert driver.find_element(*Locators.error_text_add_announcement)

    '''Создание объявления авторизованным пользователем'''
    def test_create_advertisements_user(self, driver):
        driver.get(Constants.url_doska)
        driver.find_element(*Locators.login_and_register_button).click()
        driver.find_element(*Locators.no_accaunt_button).click()

        email = f'user_{random.randint(0, 9999)}@mail.ru'
        password = '12345678'

        driver.find_element(*Locators.email_input).send_keys(email)
        driver.find_element(*Locators.password_input).send_keys(password)
        driver.find_element(*Locators.confirm_password_input).send_keys(password)

        driver.find_element(*Locators.create_accaunt_button).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.logout_button)
        )


        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.profile_button)
        )

        driver.find_element(*Locators.add_announcement).click()

        name = ''.join(random.choices(string.ascii_letters, k=5))
        description = ''.join(random.choices(string.ascii_letters, k=5))
        price = random.randint(0, 1000000)

        states = [Locators.new_product_checkbox, Locators.old_product_checkbox]

        random_city = random.choice(Constants.cities)
        random_categoty = random.choice(Constants.categories)
        random_state = random.choice(states)

        driver.find_element(*Locators.name_input).send_keys(name)
        driver.find_element(*Locators.description_input).send_keys(description)
        driver.find_element(*Locators.price_input).send_keys(price)

        driver.find_element(*Locators.city_input).click()
        random_city_locator = (Locators.random_city_text[0], 
                               Locators.random_city_text[1].format(random_city))
        driver.find_element(*random_city_locator).click()

        driver.find_element(*Locators.category_input).click()
        random_categoty_locator = (Locators.random_category_text[0], 
                               Locators.random_category_text[1].format(random_categoty))
        driver.find_element(*random_categoty_locator).click()

        driver.find_element(*random_state).click()
        
        driver.find_element(*Locators.create_button).click()
        driver.refresh()

        driver.find_element(*Locators.profile_button).click()

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.edit_button)
        )
        created_name_locator = (Locators.created_name[0], 
                               Locators.created_name[1].format(name))
        created_random_city_name_locator = (Locators.created_random_city_name[0], 
                               Locators.created_random_city_name[1].format(random_city))
        assert (driver.find_element(*created_name_locator) and 
                driver.find_element(*created_random_city_name_locator))
                