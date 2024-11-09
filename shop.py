# Отображение страницы товара
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
account_btn = driver.find_element(By.ID, "menu-item-50").click() # Нажимаем на вкладку "My Account"
field_email = driver.find_element(By.ID, "username").send_keys("tester777@mail.ru") # Заполняем поле "Email"
field_password = driver.find_element(By.ID, "password").send_keys("FgnrwrEEdw///") # Заполняем поле "Password"
login_btn = driver.find_element(By.NAME, "login").click() # Нажимаем на кнопку "Login"
shop_btn = driver.find_element(By.ID, "menu-item-40").click() # Нажимаем на вкладку "Shop"
book_html5 = driver.find_element(By.CSS_SELECTOR, "[title='Mastering HTML5 Forms']").click() # Нажимаем на книгу "HTML 5 Forms"

# Проверка, что заголовок книги называется: "HTML5 Forms"
element = driver.find_element(By.TAG_NAME, "h1") # ищем элемент
element_get_text = element.text # получили текст элемента с помощью .text
assert element_get_text == "HTML5 Forms" # добавили проверку что содержимое равно ожидаемому
driver.quit()
###
###
###
###
###
# Количество товаров в категории
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
account_btn = driver.find_element(By.ID, "menu-item-50").click() # Нажимаем на вкладку "My Account"
field_email = driver.find_element(By.ID, "username").send_keys("tester777@mail.ru") # Заполняем поле "Email"
field_password = driver.find_element(By.ID, "password").send_keys("FgnrwrEEdw///") # Заполняем поле "Password"
login_btn = driver.find_element(By.NAME, "login").click() # Нажимаем на кнопку "Login"
shop_btn = driver.find_element(By.ID, "menu-item-40").click() # Нажимаем на вкладку "Shop"
html_btn = driver.find_element(By.LINK_TEXT, "HTML").click() # Нажимаем на категорию "HTML"

# Проверка кол-ва товаров
items_count = driver.find_elements(By.CLASS_NAME, "woocommerce-LoopProduct-link")
if len(items_count) == 3:
    print("Отображается 3 товара")
else:
    print("Ошибка. Количество товаров : " + str(len(items_count)))
driver.quit()
###
###
###
###
###
# Сортировка товаров
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select # импортируем класс Select из библиотеки webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
account_btn = driver.find_element(By.ID, "menu-item-50").click() # Нажимаем на вкладку "My Account"
field_email = driver.find_element(By.ID, "username").send_keys("tester777@mail.ru") # Заполняем поле "Email"
field_password = driver.find_element(By.ID, "password").send_keys("FgnrwrEEdw///") # Заполняем поле "Password"
login_btn = driver.find_element(By.NAME, "login").click() # Нажимаем на кнопку "Login"
shop_btn = driver.find_element(By.ID, "menu-item-40").click() # Нажимаем на вкладку "Shop"

# Проверка что в селекторе выбран вариант "Default sorting"
selector_1 = driver.find_element(By.CSS_SELECTOR, "option:nth-child(1)") # Находим элемент
selector_1_get_text = selector_1.text # получили текст элемента с помощью .text
assert selector_1_get_text == "Default sorting" # добавили проверку что содержимое равно ожидаемому

# Альтернативный вариант
#selector_1 = driver.find_element(By.CSS_SELECTOR, "option:nth-child(1)") # Находим элемент
#selector_1_check = selector_1.get_attribute("value") # создали переменную, в которую поместим значение атрибута
#if selector_1_check == "menu_order": # проверяем, если выбрано значение "Default sorting"
#    print("Выбрано значение 'Default sorting'")
#else:
#    print("Выбрано другое значение")

# Сортировка товаров "Sort by price: high to low"
selector_2 = driver.find_element(By.CLASS_NAME, "orderby") # Находим селектор
select = Select(selector_2)
select.select_by_index(5) # находим элемент по порядковому номеру

# Проверка что в селекторе выбран вариант "Sort by price: high to low"
selector_3 = driver.find_element(By.CSS_SELECTOR, "option:nth-child(6)") # Находим элемент
selector_3_get_text = selector_3.text # получили текст элемента с помощью .text
assert selector_3_get_text == "Sort by price: high to low" # добавили проверку что содержимое равно ожидаемому

# Альтернативный вариант
#selector_3 = driver.find_element(By.CSS_SELECTOR, ".orderby > option:nth-child(6)") # Находим элемент
#selector_3_check = selector_3.get_attribute("value") # создали переменную, в которую поместим значение атрибута
#if selector_3_check == "price-desc": # проверяем, если выбрано значение "Sort by price: high to low"
#    print("Выбрано значение 'High to low'")
#else:
#    print("Выбрано другое значение")

driver.quit()
###
###
###
###
###
# Отображение, скидка товара
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
account_btn = driver.find_element(By.ID, "menu-item-50").click() # Нажимаем на вкладку "My Account"
field_email = driver.find_element(By.ID, "username").send_keys("tester777@mail.ru") # Заполняем поле "Email"
field_password = driver.find_element(By.ID, "password").send_keys("FgnrwrEEdw///") # Заполняем поле "Password"
login_btn = driver.find_element(By.NAME, "login").click() # Нажимаем на кнопку "Login"
shop_btn = driver.find_element(By.ID, "menu-item-40").click() # Нажимаем на вкладку "Shop"
book_android = driver.find_element(By.CSS_SELECTOR, "[title='Android Quick Start Guide']").click() # Нажимаем на книгу "Android Quick Start Guide"

# Проверка, что содержимое старой цены = "₹600.00"
price_1 = driver.find_element(By.CSS_SELECTOR, ".price > del") # ищем элемент
price_1_get_text = price_1.text # получили текст элемента с помощью .text
assert price_1_get_text == "₹600.00" # добавили проверку что содержимое равно ожидаемому

# Проверка, что содержимое новой цены = "₹450.00"
price_2 = driver.find_element(By.CSS_SELECTOR, ".price > ins") # ищем элемент
price_2_get_text = price_2.text # получили текст элемента с помощью .text
assert price_2_get_text == "₹450.00" # добавили проверку что содержимое равно ожидаемому

# Реализация явных ожиданий
book_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[title='Android Quick Start Guide']")) )
book_btn.click()

exit_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")) )
exit_btn.click()

driver.quit()
###
###
###
###
###
# Проверка цены в корзине
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
shop_btn = driver.find_element(By.ID, "menu-item-40").click() # Нажимаем на вкладку "Shop"
book_html5 = driver.find_element(By.CSS_SELECTOR, ".post-182 a:nth-child(2)").click() # Добавляем в корзину книгу "HTML5 WebApp Development"
time.sleep(1)
# Проверка, что количество товаров = "1 Item"
element_1 = driver.find_element(By.CSS_SELECTOR, ".wpmenucart-contents .cartcontents") # ищем элемент
element_1_get_text = element_1.text # получили текст элемента с помощью .text
assert element_1_get_text == "1 Item" # добавили проверку что содержимое равно ожидаемому

# Проверка, что стоимость товаров = "₹180.00"
element_2 = driver.find_element(By.CSS_SELECTOR, ".wpmenucart-contents .amount") # ищем элемент
element_2_get_text = element_2.text # получили текст элемента с помощью .text
assert element_2_get_text == "₹180.00" # добавили проверку что содержимое равно ожидаемому

basket_btn = driver.find_element(By.CLASS_NAME, "wpmenucart-contents").click() # Переходим в корзину

# Проверка, что в "Subtotal" отобразилась стоимость
subtotal = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "cart-subtotal"), "₹180.00"))

# Проверка, что в "Total" отобразилась стоимость
total = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "order-total"), "₹183.60"))

driver.quit()
###
###
###
###
###
# Работа в корзине
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
shop_btn = driver.find_element(By.ID, "menu-item-40").click() # Нажимаем на вкладку "Shop"
driver.execute_script("window.scrollBy(0, 300);") # Скроллим страницу вниз на 300 пикселей
book_1 = driver.find_element(By.CSS_SELECTOR, ".post-182 a:nth-child(2)").click() # Добавляем в корзину книгу "HTML5 WebApp Development"
time.sleep(1)
book_2 = driver.find_element(By.CSS_SELECTOR, ".post-180 a:nth-child(2)").click() # Добавляем в корзину книгу "JS Data Structures and Algorithm"
time.sleep(1)
basket_btn = driver.find_element(By.CLASS_NAME, "wpmenucart-contents").click() # Переходим в корзину
time.sleep(1)
book_1_delete = driver.find_element(By.CSS_SELECTOR, ".cart_item:nth-child(1) .remove").click() # Удаляем книгу "HTML5 WebApp Development"
time.sleep(1)
undo_btn = driver.find_element(By.LINK_TEXT, "Undo?").click() # Нажимаем на "Undo"
quantity = driver.find_element(By.CSS_SELECTOR, ".cart_item:nth-child(1) input").clear() # Очищаем поле ввода
quantity_add = driver.find_element(By.CSS_SELECTOR, ".cart_item:nth-child(1) input").send_keys("3") # Увеличиваем кол-во товара до 3 штук
update_basket = driver.find_element(By.NAME, "update_cart").click() # Нажимаем на кнопку "UPDATE BASKET"

# НЕ ПОЛУЧАЕТСЯ ПРОВЕРИТЬ МЕТОДОМ "ASSERT"-???
#element = driver.find_element(By.CSS_SELECTOR, ".cart_item:nth-child(1) input[value]")
#element_get_text = element.text # получили текст элемента с помощью .text
#assert element_get_text == "3" # добавили проверку что содержимое равно ожидаемому

# Проверка, что value элемента quantity для "JS Data Structures and Algorithm" = 3
element = driver.find_element(By.CSS_SELECTOR, ".cart_item:nth-child(1) input")
element_check = element.get_attribute("value")
if element_check == "3":
    print("Cодержимое равно ожидаемому")
else:
    print("Ошибка")

time.sleep(3)

apply_btn = driver.find_element(By.NAME, "apply_coupon").click() # Нажимаем на кнопку "APPLY COUPON"
time.sleep(1)

# Проверка, что возникло сообщение: "Please enter a coupon code."
element_1 = driver.find_element(By.CSS_SELECTOR, ".woocommerce-error > li") # ищем элемент
element_1_get_text = element_1.text # получили текст элемента с помощью .text
assert element_1_get_text == "Please enter a coupon code." # добавили проверку что содержимое равно ожидаемому

driver.quit()
###
###
###
###
###
# Покупка товара
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
shop_btn = driver.find_element(By.ID, "menu-item-40").click() # Нажимаем на вкладку "Shop"
driver.execute_script("window.scrollBy(0, 300);") # Скроллим страницу вниз на 300 пикселей
book_html5 = driver.find_element(By.CSS_SELECTOR, ".post-182 a:nth-child(2)").click() # Добавляем в корзину книгу "HTML5 WebApp Development"
time.sleep(1)
basket_btn = driver.find_element(By.CLASS_NAME, "wpmenucart-contents").click() # Переходим в корзину

# Явное ожидание кнопки "PROCEED TO CHECKOUT"
checkout_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout > a")) )
checkout_btn.click()

# Явное ожидание перед заполнением "first name"
field_firstname = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "billing_first_name")) )
field_firstname.send_keys("Anton") # Заполняем поле "First Name"

field_lastname = driver.find_element(By.ID, "billing_last_name").send_keys("Popov") # Заполняем поле "Last Name"
field_email = driver.find_element(By.ID, "billing_email").send_keys("tester777@mail.ru") # Заполняем поле "Email"
field_phone = driver.find_element(By.ID, "billing_phone").send_keys("1357924680") # Заполняем поле "Phone"

# Заполнение селектора "Country"
selector_country = driver.find_element(By.ID, "s2id_billing_country").click() # Нажимаем на селектор
input_field = driver.find_element(By.ID, "s2id_autogen1_search").send_keys("Russia") # Вводим название в поле ввода
click_selection = driver.find_element(By.CLASS_NAME, "select2-match").click() # Нажимаем на вариант в поле ввода

field_address = driver.find_element(By.ID, "billing_address_1").send_keys("Nevsky Prospect 55") # Заполняем поле "Address"
field_city = driver.find_element(By.ID, "billing_city").send_keys("Saint Petersburg") # Заполняем поле "Town / City"
field_state = driver.find_element(By.ID, "billing_state").send_keys("Russia") # Заполняем поле "State / County"
field_zip = driver.find_element(By.ID, "billing_postcode").send_keys("191025") # Заполняем поле "Postcode / ZIP"
time.sleep(1)
driver.execute_script("window.scrollBy(0, 600);") # Скроллим страницу вниз на 600 пикселей
time.sleep(1)
radio_check = driver.find_element(By.CSS_SELECTOR, "[value='cheque']").click() # Выбираем radiobutton "Check Payments"
time.sleep(3)
placeorder_btn = driver.find_element(By.ID, "place_order").click() # Нажимаем на кнопку "PLACE ORDER"
time.sleep(3)

# Явное ожидание, что отображается надпись "Thank you. Your order has been received."
title_check = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))

# Явное ожидание, что в Payment Method отображается текст "Check Payments"
title_check_2 = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method > strong"), "Check Payments"))

driver.quit()
