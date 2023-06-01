# Adding a comment
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

# Open link
driver.get("https://practice.automationtesting.in/")
# Scrolling down the page
driver.execute_script("window.scrollBy(0, 600);")
# Clicking on the title of the book "Selenium Ruby"
selenium_ruby_book = driver.find_element_by_css_selector('[title="Selenium Ruby"]')
selenium_ruby_book.click()
# Going to the "REVIEWS" tab
driver.execute_script("window.scrollBy(0, 300);")
reviews_btn = driver.find_element_by_css_selector("li.reviews_tab")
reviews_btn.click()
# Setting 5 stars
driver.execute_script("window.scrollBy(0, 600);")
all_stars = driver.find_element_by_css_selector("a.star-5")
all_stars.click()
# Filling in the fields "Review", "Name", "Email"
review_field = driver.find_element_by_name("comment")
review_field.send_keys("Nice Book!")
name_field = driver.find_element_by_css_selector("input#author")
name_field.send_keys("Irene")
email_field = driver.find_element_by_css_selector("input#email")
email_field.send_keys("test22@gmail.com")
# Clicking on the "SUBMIT" button
submit_btn = driver.find_element_by_class_name("submit")
submit_btn.click()

driver.quit()
