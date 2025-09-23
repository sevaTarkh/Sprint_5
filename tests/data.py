from selenium.webdriver.common.by import By

class Locators:
    Login_and_register_button = ".//button[text()='Вход и регистрация']"
    No_accaunt_button = ".//button[text()='Нет аккаунта']"
    Email_input = ".//input[@name='email']"
    Password_input = ".//input[@name='password']"
    Confirm_password_input = ".//input[@name='submitPassword']"
    Create_accaunt_button =  ".//button[text()='Создать аккаунт']"
    Logout_button =  ".//button[text()='Выйти']"
    Login_button = ".//button[text()='Войти']"
    Error_text =  ".//span[text()='Ошибка']"
    username =  "//h3[text()='User.']"
    logo =  "svgSmall"
    Red_border =  'input_inputError__fLUP9'
    Add_announcement = ".//button[text()='Разместить объявление']"
    Name_input = "//input[@name='name']"
    Category_input = "//input[@name='category']/following-sibling::*[1]"
    City_input = "//input[@name='city']/following-sibling::*[1]"
    Description_input = "//textarea[@name='description']"
    Price_input = "//input[@name='price']"
    Create_button = ".//button[text()='Опубликовать']"
    New_product_checkbox = "//label[text()='Новый']/preceding-sibling::*[1]"
    Old_product_checkbox = "//label[text()='Б/У']/preceding-sibling::*[1]"
    Profile_button = "circleSmall"
    My_profile_text = "//h1[text()='Мой профиль']"
    Error_text_add_announcement = "//form[@class='popUp_shell__LuyqR']//h1[text()='Чтобы разместить объявление, авторизуйтесь']"

class Constants:
    url_doska = "https://qa-desk.stand.praktikum-services.ru/"
    cities = ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Казань', 'Нижний Новгород']
    categories = ['Авто', 'Книги', 'Садоводство', 'Хобби', 'Технологии']

