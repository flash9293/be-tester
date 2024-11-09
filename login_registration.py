# Регистрация аккаунта
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
account_btn = driver.find_element(By.ID, "menu-item-50").click() # Нажимаем на вкладку "My Account"
field_email = driver.find_element(By.ID, "reg_email").send_keys("tester777@mail.ru") # Заполняем поле "Email"
field_password = driver.find_element(By.ID, "reg_password").send_keys("FgnrwrEEdw///") # Заполняем поле "Password"
register_btn = driver.find_element(By.NAME, "register").click() # Нажимаем на кнопку "Register"
time.sleep(5)
driver.quit()
###
###
###
###
###
# Логин в систему
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
account_btn = driver.find_element(By.ID, "menu-item-50").click() # Нажимаем на вкладку "My Account"
field_email = driver.find_element(By.ID, "username").send_keys("tester777@mail.ru") # Заполняем поле "Email"
field_password = driver.find_element(By.ID, "password").send_keys("FgnrwrEEdw///") # Заполняем поле "Password"
login_btn = driver.find_element(By.NAME, "login").click() # Нажимаем на кнопку "Login"

# Проверка, что на странице есть элемент"Logout"
element = driver.find_element(By.LINK_TEXT, "Logout") # ищем элемент
element_get_text = element.text # получили текст элемента с помощью .text
assert element_get_text == "Logout" # добавили проверку что содержимое равно ожидаемому
driver.quit()
