# Добавление комментария
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);") # Скроллим страницу вниз на 600 пикселей
book_selenium = driver.find_element(By.CSS_SELECTOR, "[title='Selenium Ruby']").click() # Нажимаем на книгу "Selenium Ruby"
reviews_btn = driver.find_element(By.CLASS_NAME, "reviews_tab").click() # Нажимаем на вкладку "REVIEWS"
star_btn = driver.find_element(By.CLASS_NAME, "star-5").click() # Ставим 5 звезд
field_review = driver.find_element(By.ID, "comment").send_keys("Nice book!") # Заполняем поле "Review"
field_name = driver.find_element(By.ID, "author").send_keys("Anton") # Заполняем поле "Name"
field_email = driver.find_element(By.ID, "email").send_keys("test@mail.ru") # Заполняем поле "Email"
submit_btn = driver.find_element(By.ID, "submit").click() # Нажимаем на кнопку "SUBMIT"
driver.quit()

