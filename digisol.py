from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def catch(html):
    with open("catch.html","w",encoding="utf-8") as catch:
        catch.write(html)

option=Options()
option.add_argument("-headless")
driver=webdriver.Chrome(options=option)
driver.implicitly_wait(10)
router_address="192.168.1.1"
driver.get(f"http://{router_address}/")
try:
    name_id=driver.find_element(By.ID,"username1")
    password_id=driver.find_element(By.ID,"psd1")
    button = driver.find_element(By.XPATH, "//input[@onclick='on_submit();']")
    # management = driver.find_element(By.XPATH, "//input[@onclick='on_catolog(4);']")

    unique_code_id=driver.find_element(By.ID,"check_code")
    verification_code_id=driver.find_element(By.ID,"verification_code")
    code=unique_code_id.get_attribute("value")

    print(code)
    name_id.send_keys("admin")
    password_id.send_keys("admin12345")
    verification_code_id.send_keys(code)
    button.click()
except Exception as e:
    print("already Logged in..")

driver.switch_to.frame("topFrame")
management=driver.find_element(By.XPATH,"//span[text()='Management']")
management.click()
device_manage=driver.find_element(By.XPATH,"//span[text()='Device Manage']")
device_manage.click()
driver.switch_to.parent_frame()
driver.switch_to.frame("mainFrame")
reboot_btn = driver.find_element(By.XPATH,"//input[@value='Commit and Reboot']")
reboot_btn.click()
print('Reboot sucessfull')
