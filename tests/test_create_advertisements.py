import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestCreatingAdvertisements:
    url_doska = "https://qa-desk.stand.praktikum-services.ru/"

    LOCATORS = {
        'Вход и регистрация':".//button[text()='Вход и регистрация']",
        'Нет аккаунта': ".//button[text()='Нет аккаунта']",
        'email': ".//input[@name='email']",
        'Пароль': ".//input[@name='password']",
        'Повтор пароля':".//input[@name='submitPassword']",
        'Создать аккаунт': ".//button[text()='Создать аккаунт']", 
        'Войти': ".//button[text()='Войти']",
        'Разместить объявление': ".//button[text()='Разместить объявление']",
        'Название': "//input[@name='name']",
        'Категория': "//input[@name='category']/following-sibling::*[1]",
        'Город': "//input[@name='city']/following-sibling::*[1]",
        'Описание': "//textarea[@name='description']",
        'Стоимость': "//input[@name='price']",
        'Опубликовать': ".//button[text()='Опубликовать']",
        'Состояние товара - новый': "//label[text()='Новый']/preceding-sibling::*[1]",
        'Состояние товара - Б/У': "//label[text()='Б/У']/preceding-sibling::*[1]",
        'Выйти': ".//button[text()='Выйти']",
        'Профиль': "circleSmall",
        'User.': "//h3[text()='User.']",
        'logo': "svgSmall",
        'Мой профиль':  "//h1[text()='Мой профиль']",
        'Чтобы разместить объявление, авторизуйтесь': "//form[@class='popUp_shell__LuyqR']//h1[text()='Чтобы разместить объявление, авторизуйтесь']", 
    }

    '''Создание объявления неавторизованным пользователем'''
    def test_create_advertisements_unauthorized_user(self, driver):
        driver.get(self.url_doska)
        driver.find_element(By.XPATH, self.LOCATORS['Разместить объявление']).click()

        assert driver.find_element(By.XPATH, self.LOCATORS['Чтобы разместить объявление, авторизуйтесь'])

    '''Создание объявления авторизованным пользователем'''
    def test_create_advertisements_user(self, driver):
        driver.get(self.url_doska)
        driver.find_element(By.XPATH, self.LOCATORS['Вход и регистрация']).click()
        driver.find_element(By.XPATH, self.LOCATORS["Нет аккаунта"]).click()

        email = f'user_{random.randint(0, 9999)}@mail.ru'
        password = '12345678'

        driver.find_element(By.XPATH, self.LOCATORS["email"]).send_keys(email)
        driver.find_element(By.XPATH, self.LOCATORS["Пароль"]).send_keys(password)
        driver.find_element(By.XPATH, self.LOCATORS["Повтор пароля"]).send_keys(password)

        driver.find_element(By.XPATH, self.LOCATORS["Создать аккаунт"]).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.LOCATORS["Выйти"]))
        )
        assert (driver.find_element(By.CLASS_NAME, self.LOCATORS['Профиль']) and
                driver.find_element(By.CLASS_NAME, self.LOCATORS['logo']))

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.LOCATORS['Профиль']))
        )
        assert (driver.find_element(By.XPATH, self.LOCATORS['User.']) and
                driver.find_element(By.CLASS_NAME, self.LOCATORS['logo']))

        driver.find_element(By.XPATH, self.LOCATORS['Разместить объявление']).click()

        name = ''.join(random.choices(string.ascii_letters, k=5))
        description = ''.join(random.choices(string.ascii_letters, k=5))
        price = random.randint(0, 1000000)
        cities = ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Казань', 'Нижний Новгород']
        categories = ['Авто', 'Книги', 'Садоводство', 'Хобби', 'Технологии']
        states = [self.LOCATORS['Состояние товара - новый'], self.LOCATORS['Состояние товара - Б/У']]

        random_city = random.choice(cities)
        random_categoty = random.choice(categories)
        random_state = random.choice(states)

        driver.find_element(By.XPATH, self.LOCATORS['Название']).send_keys(name)
        driver.find_element(By.XPATH, self.LOCATORS['Описание']).send_keys(description)
        driver.find_element(By.XPATH, self.LOCATORS['Стоимость']).send_keys(price)

        driver.find_element(By.XPATH, self.LOCATORS['Город']).click()
        driver.find_element(By.XPATH, f"//span[text()='{random_city}']").click()

        driver.find_element(By.XPATH, self.LOCATORS['Категория']).click()
        driver.find_element(By.XPATH, f"//span[text()='{random_categoty}']").click()

        driver.find_element(By.XPATH, self.LOCATORS['Город']).click()
        driver.find_element(By.XPATH, random_state).click()
        
        driver.find_element(By.XPATH, self.LOCATORS['Опубликовать']).click()
        driver.refresh()

        driver.find_element(By.CLASS_NAME, self.LOCATORS["Профиль"]).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.LOCATORS['Мой профиль']))
        )
        # прошу подсказку, без слипа не получается пройти тест, явное ожидание также не помогает
        time.sleep(1)
        assert (driver.find_element(By.XPATH, f"//h2[text()='{name}']") and 
                driver.find_element(By.XPATH, f"//h3[text()='{random_city}']"))
                