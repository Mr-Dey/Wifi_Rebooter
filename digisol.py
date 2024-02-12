from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.implicitly_wait(10)
router_address="192.168.1.1"
driver.get(f"http://{router_address}/")
name_id=driver.find_element(By.ID,"username1")
password_id=driver.find_element(By.ID,"psd1")
button = driver.find_element(By.XPATH, "//input[@onclick='on_submit();']")

unique_code_id=driver.find_element(By.ID,"check_code")
verification_code_id=driver.find_element(By.ID,"verification_code")
code=unique_code_id.get_attribute("value")

print(code)
name_id.send_keys("admin")
password_id.send_keys("admin12345")
verification_code_id.send_keys(code)
button.click()
