# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    """Фикстура для создания и закрытия драйвера Chrome"""
    # Настройки Chrome
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Максимизировать окно
    chrome_options.add_argument("--disable-extensions")  # Отключить расширения
    
    # Создание драйвера
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    
    yield driver  # Возвращаем драйвер тесту
    
    # Закрытие браузера после теста
    driver.quit()
