import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Locators, Constants

class TestCreatingAdvertisements:

    '''Создание объявления неавторизованным пользователем'''
    def test_create_advertisements_unauthorized_user(self, driver):
        driver.get(Constants.url_doska)
        driver.find_element(By.XPATH, Locators.Add_announcement).click()

        assert driver.find_element(By.XPATH, Locators.Error_text_add_announcement)

    '''Создание объявления авторизованным пользователем'''
    def test_create_advertisements_user(self, driver):
        driver.get(Constants.url_doska)
        driver.find_element(By.XPATH, Locators.Login_and_register_button).click()
        driver.find_element(By.XPATH, Locators.No_accaunt_button).click()

        email = f'user_{random.randint(0, 9999)}@mail.ru'
        password = '12345678'

        driver.find_element(By.XPATH, Locators.Email_input).send_keys(email)
        driver.find_element(By.XPATH, Locators.Password_input).send_keys(password)
        driver.find_element(By.XPATH, Locators.Confirm_password_input).send_keys(password)

        driver.find_element(By.XPATH, Locators.Create_accaunt_button).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Locators.Logout_button))
        )


        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.CLASS_NAME, Locators.Profile_button))
        )

        driver.find_element(By.XPATH, Locators.Add_announcement).click()

        name = ''.join(random.choices(string.ascii_letters, k=5))
        description = ''.join(random.choices(string.ascii_letters, k=5))
        price = random.randint(0, 1000000)

        states = [Locators.New_product_checkbox, Locators.Old_product_checkbox]

        random_city = random.choice(Constants.cities)
        random_categoty = random.choice(Constants.categories)
        random_state = random.choice(states)

        driver.find_element(By.XPATH, Locators.Name_input).send_keys(name)
        driver.find_element(By.XPATH, Locators.Description_input).send_keys(description)
        driver.find_element(By.XPATH, Locators.Price_input).send_keys(price)

        driver.find_element(By.XPATH, Locators.City_input).click()
        driver.find_element(By.XPATH, f"//span[text()='{random_city}']").click()

        driver.find_element(By.XPATH, Locators.Category_input).click()
        driver.find_element(By.XPATH, f"//span[text()='{random_categoty}']").click()

        driver.find_element(By.XPATH, random_state).click()
        
        driver.find_element(By.XPATH, Locators.Create_button).click()
        driver.refresh()

        driver.find_element(By.CLASS_NAME, Locators.Profile_button).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Locators.My_profile_text))
        )
        # прошу подсказку, без слипа не получается пройти тест, явное ожидание также не помогает
        time.sleep(1)
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,"//button[@class='editButton']"))
        )
        assert (driver.find_element(By.XPATH, f"//h2[text()='{name}']") and 
                driver.find_element(By.XPATH, f"//h3[text()='{random_city}']"))
                