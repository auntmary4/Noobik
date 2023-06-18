from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import pytest
@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("http://185.67.95.60/")  # Передаем ссылку драйверу
    yield driver  # Драйвер передается тесту, начинается тест
    driver.close()  # Закрываем браузер


def test_auth(driver):
    login = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail")))  # дожидаемся пока логин загрузиться
    login.send_keys('student@protei.ru')  # Вводим логин
    password = driver.find_element(value="loginPassword")  # Ищем поле с паролем
    password.send_keys('student')  # Вводим пароль
    enter = driver.find_element(value="authButton")  # Ищем кнопку вход
    enter.click()  # Кликаем на неё
    main_title = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.TAG_NAME, "h3")))  # Дожидаемся загрузки
    assert main_title.text == "Добро пожаловать!"  # Сравниваем элементы
