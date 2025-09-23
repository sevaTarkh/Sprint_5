import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Locators, Constants

class TestLoginUser:

    '''Login пользователя'''
    def test_login_user(self, driver):
        driver.get(Constants.url_doska)
        driver.find_element(By.XPATH, Locators.Login_and_register_button).click()
        driver.find_element(By.XPATH, Locators.No_accaunt_button).click()

        email = f'user_{random.randint(0, 9999)}@mail.ru'
        password = '12345678'

        driver.find_element(By.XPATH, Locators.Email_input).send_keys(email)
        driver.find_element(By.XPATH, Locators.Password_input).send_keys(password)
        driver.find_element(By.XPATH, Locators.Confirm_password_input).send_keys(password)

        driver.find_element(By.XPATH, Locators.Create_accaunt_button).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, Locators.Logout_button))
        )

        driver.find_element(By.XPATH, Locators.Logout_button).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, Locators.Login_and_register_button))
        )
        driver.find_element(By.XPATH, Locators.Login_and_register_button).click()

        driver.find_element(By.XPATH, Locators.Email_input).send_keys(email)
        driver.find_element(By.XPATH, Locators.Password_input).send_keys(password)

        driver.find_element(By.XPATH, Locators.Login_button).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, Locators.username))
        )
        assert (driver.find_element(By.XPATH, Locators.username) and
                driver.find_element(By.CLASS_NAME, Locators.logo))

    '''Logout пользователя'''
    def test_logout_user(self, driver):
        driver.get(Constants.url_doska)
        driver.find_element(By.XPATH, Locators.Login_and_register_button).click()
        driver.find_element(By.XPATH, Locators.No_accaunt_button).click()

        email = f'user_{random.randint(0, 9999)}@mail.ru'
        password = '12345678'

        driver.find_element(By.XPATH, Locators.Email_input).send_keys(email)
        driver.find_element(By.XPATH, Locators.Password_input).send_keys(password)
        driver.find_element(By.XPATH, Locators.Confirm_password_input).send_keys(password)

        driver.find_element(By.XPATH, Locators.Create_accaunt_button).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, Locators.Logout_button))
        )

        driver.find_element(By.XPATH, Locators.Logout_button).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, Locators.Login_and_register_button))
        )
        assert driver.find_element(By.XPATH, Locators.Login_and_register_button)