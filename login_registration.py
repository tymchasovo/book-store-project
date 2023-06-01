# Registration

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

# Open link
driver.get("https://practice.automationtesting.in/")
# Going to the "My Account" section
my_account_btn = driver.find_element_by_link_text("My Account")
my_account_btn.click()
# Email for registration
email_field = driver.find_element_by_css_selector("input#reg_email")
email_field.send_keys("test02@gmail.com")
# Password for registration
password_field = driver.find_element_by_css_selector("input#reg_password")
password_field.send_keys("i-tymchasovo4")
# Clicking on the "Register" button
register_btn = WebDriverWait(driver, 10).until(
     EC.element_to_be_clickable((By.NAME, "register")))
register_btn.click()

driver.quit()



# Login

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

# Open link
driver.get("https://practice.automationtesting.in/")
# Going to the "My Account" section
my_account_btn = driver.find_element_by_link_text("My Account")
my_account_btn.click()
# Email for login
email_field = driver.find_element_by_id("username")
email_field.send_keys("test02@gmail.com")
# Password for login
password_field = driver.find_element_by_id("password")
password_field.send_keys("i-tymchasovo4")
# Clicking on the "Login" button
login_btn = driver.find_element_by_name("login")
login_btn.click()
# Checking the "Logout" element on the page
try:
    logout = driver.find_element_by_link_text("Logout")
    print("Элемент Logout присутствует на странице")
except NoSuchElementException:
    print("Элемент Logout отсутствует")

driver.quit()
