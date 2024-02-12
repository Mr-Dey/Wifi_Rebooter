from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
router_address=input("Enter router gateway.\n")
router_address=f"http://{router_address}/"

password_user_id="userName"
password_field_id="pcPassword"
login_btn_id="loginBtn"
menu_btn_id="menu_tools"
reboot_btn0="menu_restart"
user="admin"
password="admin123"

driver.get(router_address)
print(driver)

#get
login_feild_user=driver.find_element(By.ID, password_user_id)
login_feild_pass=driver.find_element(By.ID, password_field_id)
login_btn=driver.find_element(By.ID,login_btn_id)
login_feild_pass.send_keys(password)
login_btn.click()
# Get the current window handle
current_handle = driver.current_window_handle

# Perform actions that lead to opening a new window
# For example, click a link that opens a new window

# Switch to the new window
for handle in driver.window_handles:
    if handle != current_handle:
        driver.switch_to.window(handle)
        break

time.sleep(2)
menu_btn=driver.find_element(By.ID,menu_btn_id)
# menu_btn.click()
# reboot_btn0=driver.find_element(By.ID,reboot_btn0)

#set
# login_feild_user.send_keys(user)

#action
# reboot_btn0.click()
# print(login_feild.text)
