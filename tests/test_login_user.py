import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestLoginUser:
    url_doska = "https://qa-desk.stand.praktikum-services.ru/"

    LOCATORS = {
        'Вход и регистрация':".//button[text()='Вход и регистрация']",
        'Нет аккаунта': ".//button[text()='Нет аккаунта']",
        'email': ".//input[@name='email']",
        'Пароль': ".//input[@name='password']",
        'Повтор пароля':".//input[@name='submitPassword']",
        'Создать аккаунт': ".//button[text()='Создать аккаунт']", 
        'Выйти': ".//button[text()='Выйти']",
        'Войти': ".//button[text()='Войти']",
        'User.': "//h3[text()='User.']",
        'logo': "svgSmall",
    }

    '''Login пользователя'''
    def test_login_user(self, driver):
        driver.get(self.url_doska)
        driver.find_element(By.XPATH, self.LOCATORS['Вход и регистрация']).click()
        driver.find_element(By.XPATH, self.LOCATORS["Нет аккаунта"]).click()

        email = f'user_{random.randint(0, 9999)}@mail.ru'
        password = '12345678'

        driver.find_element(By.XPATH, self.LOCATORS["email"]).send_keys(email)
        driver.find_element(By.XPATH, self.LOCATORS["Пароль"]).send_keys(password)
        driver.find_element(By.XPATH, self.LOCATORS["Повтор пароля"]).send_keys(password)

        driver.find_element(By.XPATH, self.LOCATORS["Создать аккаунт"]).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, self.LOCATORS["Выйти"]))
        )
        assert (driver.find_element(By.XPATH, self.LOCATORS['User.']) and
                driver.find_element(By.CLASS_NAME, self.LOCATORS['logo']))
        driver.find_element(By.XPATH, self.LOCATORS["Выйти"]).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, self.LOCATORS['Вход и регистрация']))
        )
        driver.find_element(By.XPATH, self.LOCATORS['Вход и регистрация']).click()

        driver.find_element(By.XPATH, self.LOCATORS["email"]).send_keys(email)
        driver.find_element(By.XPATH, self.LOCATORS["Пароль"]).send_keys(password)

        driver.find_element(By.XPATH, self.LOCATORS['Войти']).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, self.LOCATORS['User.']))
        )
        assert (driver.find_element(By.XPATH, self.LOCATORS['User.']) and
                driver.find_element(By.CLASS_NAME, self.LOCATORS['logo']))


    '''Logout пользователя'''
    def test_logout_user(self, driver):
        driver.get(self.url_doska)
        driver.find_element(By.XPATH, self.LOCATORS['Вход и регистрация']).click()
        driver.find_element(By.XPATH, self.LOCATORS["Нет аккаунта"]).click()

        email = f'user_{random.randint(0, 9999)}@mail.ru'
        password = '12345678'

        driver.find_element(By.XPATH, self.LOCATORS["email"]).send_keys(email)
        driver.find_element(By.XPATH, self.LOCATORS["Пароль"]).send_keys(password)
        driver.find_element(By.XPATH, self.LOCATORS["Повтор пароля"]).send_keys(password)

        driver.find_element(By.XPATH, self.LOCATORS["Создать аккаунт"]).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, self.LOCATORS["Выйти"]))
        )
        assert (driver.find_element(By.XPATH, self.LOCATORS['User.']) and
                driver.find_element(By.CLASS_NAME, self.LOCATORS['logo']))
        driver.find_element(By.XPATH, self.LOCATORS["Выйти"]).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, self.LOCATORS['Вход и регистрация']))
        )
        assert driver.find_element(By.XPATH, self.LOCATORS['Вход и регистрация'])