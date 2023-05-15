# # Product page display
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# # Open link
# driver.get("https://practice.automationtesting.in/")
# # Login
# my_account_btn = driver.find_element_by_link_text("My Account")
# my_account_btn.click()
# email_field = driver.find_element_by_id("username")
# email_field.send_keys("test02@gmail.com")
# password_field = driver.find_element_by_id("password")
# password_field.send_keys("i-tymchasovo4")
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# # Going to the "Shop" section
# shop_btn = driver.find_element_by_link_text("Shop")
# shop_btn.click()
# driver.execute_script("window.scrollBy(0, 300);")
# # Opening the book "HTML5 Forms"
# book_html = driver.find_element_by_css_selector('[title="Mastering HTML5 Forms"]')
# book_html.click()
# # Checking the book title
# title = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h1.product_title.entry-title"), "HTML5 Forms"))
# print("Текст заголовка совпадает с названием книги")
#
# driver.quit()



# # Number of products in the category
#
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# # Open link
# driver.get("https://practice.automationtesting.in/")
# # Login
# my_account_btn = driver.find_element_by_link_text("My Account")
# my_account_btn.click()
# email_field = driver.find_element_by_id("username")
# email_field.send_keys("test02@gmail.com")
# password_field = driver.find_element_by_id("password")
# password_field.send_keys("i-tymchasovo4")
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# # Going to the "Shop" section
# shop_btn = driver.find_element_by_link_text("Shop")
# shop_btn.click()
# # Opening the "HTML" category
# html_category = driver.find_element_by_link_text("HTML")
# html_category.click()
# # Checking that there are 3 products in category
# products = driver.find_elements_by_css_selector("img.attachment-shop_catalog.size-shop_catalog.wp-post-image")
# if len(products) == 3:
#     print("Количество товаров в категории равно 3")
# else:
#     print("Количество товаров в категории не соответствует заданному")
#
# driver.quit()



# # Sorting
#
# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# # Open link
# driver.get("https://practice.automationtesting.in/")
# # Login
# my_account_btn = driver.find_element_by_link_text("My Account")
# my_account_btn.click()
# email_field = driver.find_element_by_id("username")
# email_field.send_keys("test02@gmail.com")
# password_field = driver.find_element_by_id("password")
# password_field.send_keys("i-tymchasovo4")
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# # Going to the "Shop" section
# shop_btn = driver.find_element_by_link_text("Shop")
# shop_btn.click()
# # Checking that the default sorting option is selected
# select = driver.find_element_by_css_selector('select.orderby')
# selected_option = select.find_element_by_css_selector('option[selected="selected"]')
# if selected_option.get_attribute('value') == 'menu_order':
#     print('По умолчанию выбран фильтр "Default sorting"')
# else:
#     print('По умолчанию НЕ выбран фильтр "Default sorting"')
# driver.execute_script("window.scrollBy(0, 200);")
# # Sorting goods by price from higher to lower
# select_sort = driver.find_element_by_css_selector("select.orderby")
# select = Select(select_sort)
# select.select_by_index(5)
# time.sleep(3)
# # Setting a variable with the locator of the main sorting selector
# select = Select(driver.find_element_by_css_selector('select.orderby'))
# selected_option = driver.find_element_by_css_selector('option[selected="selected"]')
# # Checking that the sorting option is selected by price from higher to lower
# if selected_option.get_attribute('value') == 'price-desc':
#     print('Выбран фильтр "Sort by price: high to low"')
# else:
#     print('Выбран другой фильтр')
#
# driver.quit()



# # Display, product discount
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# # Open link
# driver.get("https://practice.automationtesting.in/")
# # Login
# my_account_btn = driver.find_element_by_link_text("My Account")
# my_account_btn.click()
# email_field = driver.find_element_by_id("username")
# email_field.send_keys("test02@gmail.com")
# password_field = driver.find_element_by_id("password")
# password_field.send_keys("i-tymchasovo4")
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# # Going to the "Shop" section
# shop_btn = driver.find_element_by_link_text("Shop")
# shop_btn.click()
# # Opening the book "Android Quick Start Guide"
# android_guide_book = driver.find_element_by_css_selector('[title="Android Quick Start Guide"]')
# android_guide_book.click()
# # Checking that the old price is 600.00₹
# old_price_element = driver.find_element_by_css_selector('del > .amount')
# assert old_price_element.text == "₹600.00"
# print("Старая цена = ₹600.00")
# # Checking that the new price is 450.00₹
# new_price_element = driver.find_element_by_css_selector('ins > .amount')
# assert new_price_element.text == "₹450.00"
# print("Новая цена = ₹450.00")
# # Clicking on the book cover
# book_cover = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# book_cover.click()
# # Closing the preview mode by clicking on the cross
# book_cover_close = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# book_cover_close.click()
#
# driver.quit()



# # Checking price in the cart
#
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# # Open link
# driver.get("https://practice.automationtesting.in/")
# # Clicking on the Shop tab
# shop_btn = driver.find_element_by_link_text("Shop")
# shop_btn.click()
# driver.execute_script("window.scrollBy(0, 600);")
# # Adding a book to the cart
# mastering_js_book = driver.find_element_by_css_selector('[data-product_id="165"]')
# mastering_js_book.click()
# time.sleep(5)
# # Checking that next to the cart icon, the number of products = "1 Item", and the cost = "$350.00"
# amount_items = driver.find_element_by_css_selector("span.cartcontents")
# price_element = driver.find_element_by_css_selector("a .amount:nth-child(3)")
# assert amount_items.text == "1 Item"
# assert price_element.text == "₹350.00"
# print("В корзине 1 товар, стоимостью ₹350.00")
# # Moving to the cart
# cart_btn = driver.find_element_by_css_selector('[title="View Basket"]')
# cart_btn.click()
# # Checking that the Subtotal shows the cost
# subtotal_element = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount"), "₹350.00"))
# print("Стоимость товара отображается в Subtotal")
# # Checking that the Total shows the cost
# total_element = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount"), "₹357.00"))
# print("Стоимость товара отображается в Total")
#
# driver.quit()


# # Buying an item
#
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# # Open link
# driver.get("https://practice.automationtesting.in/")
# # Click on the Shop tab and scroll down
# shop_btn = driver.find_element_by_link_text("Shop")
# shop_btn.click()
# driver.execute_script("window.scrollBy(0, 300);")
# # Adding a book to the cart
# mastering_js_book = driver.find_element_by_css_selector('[data-product_id="165"]')
# mastering_js_book.click()
# time.sleep(2)
# # Moving to the cart
# cart_btn = driver.find_element_by_css_selector('[title="View Basket"]')
# cart_btn.click()
# # Clicking on "PROCEED TO CHECKOUT"
# time.sleep(3)
# proceed_checkout_btn = driver.find_element_by_css_selector("a.checkout-button")
# proceed_checkout_btn.click()
# # Filling in all required fields in the form
# time.sleep(2)
# first_name_field = driver.find_element_by_id("billing_first_name")
# first_name_field.send_keys("Irene")
# last_name_field = driver.find_element_by_id("billing_last_name")
# last_name_field.send_keys("Tymchasovo")
# email_field = driver.find_element_by_id("billing_email")
# email_field.send_keys("test02@gmail.com")
# phone_field = driver.find_element_by_id("billing_phone")
# phone_field.send_keys("9654453421")
# driver.execute_script("window.scrollBy(0, 500);")
# time.sleep(1)
# select_country = driver.find_element_by_id("s2id_billing_country")
# select_country.click()
# country_search = driver.find_element_by_css_selector("input.select2-input#s2id_autogen1_search")
# country_search.send_keys("Russia")
# chosen_country = driver.find_element_by_css_selector("ul .select2-result")
# chosen_country.click()
# address_field = driver.find_element_by_id("billing_address_1")
# address_field.send_keys("Bolshaya Zelenina Street 19")
# city_field = driver.find_element_by_id("billing_city")
# city_field.send_keys("Saint Petersburg")
# state_field = driver.find_element_by_id("billing_state")
# state_field.send_keys("-")
# postcode_field = driver.find_element_by_id("billing_postcode")
# postcode_field.send_keys("194223")
# # Select payment method "CHECK PAYMENTS"
# time.sleep(5)
# driver.execute_script("window.scrollBy(0, 600);")
# checkbox = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "[value='cheque']")))
# checkbox.click()
# # Clicking on "PLACE ORDER"
# place_order_btn = driver.find_element_by_id("place_order")
# place_order_btn.click()
# # Checking the display of the label "Thank you. Your order has been received."
# label = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"),
#                                      "Thank you. Your order has been received."))
# print("Отображается надпись о подтверждении заказа")
# # Checking that the text "Check Payments" is displayed in the Payment Method
# payment_method = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "li.method > strong"), "Check Payments"))
# print("Способ оплаты - Check Payments")
#
# driver.quit()