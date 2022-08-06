import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

web_driver_path = "C:\Development/chromedriver.exe"
driver = webdriver.Chrome(web_driver_path)

driver.get("https://www.linkedin.com/")

sign_in = driver.find_element(By.XPATH, "/html/body/nav/div/a[2]")
sign_in.click()
user_name = driver.find_element(By.ID, "username")
user_name.send_keys("sarunasj82@gmail.com")
password = driver.find_element(By.ID, "password")
password.send_keys("**********")
sign_in_account = driver.find_element(By.XPATH, "//*[@id='organic-div']/form/div[3]/button")
sign_in_account.click()
# security_phone = driver.find_element(By.ID, "phone-input")
# security_phone.send_keys("********")
search = driver.find_element(By.XPATH, "//*[@id='global-nav-typeahead']/input")
search.send_keys("Python developer")
search.send_keys(Keys.ENTER)
time.sleep(5)

jobs = driver.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[1]')
jobs.click()
time.sleep(5)
easy_apply = driver.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[8]')
easy_apply.click()
time.sleep(5)

jobs_list = driver.find_elements(By.CSS_SELECTOR, '.jobs-search-results__list list-style-none')
for offer in jobs_list:
    offer.click()
    time.sleep(3)


    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
        apply_button.click()
        time.sleep(5)

        phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys("********")

        next_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-button__text")
        next_button.click()

        next_button.click()
        next_button.click()
    except NoSuchElementException:
        continue

time.sleep(10)
driver.quit()
