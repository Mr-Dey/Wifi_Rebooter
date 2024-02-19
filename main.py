from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def catch(html):
    with open("page1.html","w", encoding="utf-8") as x:
        x.write(html)

driver=webdriver.Chrome()
router_address="http://192.168.0.3/"

password_user_id="userName"
password_field_id="pcPassword"
login_btn_id="loginBtn"
# menu_btn_id="menu_tools"
# reboot_btn0="menu_restart"
reboot_btn_id="button_reboot"
user="admin"
password="admin123"

driver.get(router_address)
driver.implicitly_wait(10)


login_feild_user=driver.find_element(By.ID, password_user_id)
login_feild_pass=driver.find_element(By.ID, password_field_id)
login_btn=driver.find_element(By.ID,login_btn_id)
login_feild_pass.send_keys(password)

login_btn.click()
driver.switch_to.frame("frame1")
menu_btn=driver.find_element(By.ID,"menu_tools")
menu_btn.click()
menu_restart=driver.find_element(By.ID,"menu_restart")
menu_restart.click()
driver.switch_to.parent_frame()
driver.switch_to.frame("frame2")
reboot=driver.find_element(By.ID,"button_reboot")
reboot.click()
time.sleep(5)

# catch(driver.page_source)
