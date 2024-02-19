from selenium import webdriver
from selenium.webdriver.common.by import By

#to catch the page source if needed.
def catch(html):
    with open("page1.html","w", encoding="utf-8") as x:
        x.write(html)
        
def my_tplink():
    driver=webdriver.Chrome()

    #Confidential
    router_address="http://192.168.0.3/"
    username="admin"
    password="admin123"

    #loadpage
    driver.get(router_address)
    driver.implicitly_wait(10)

    #ids
    user_id="userName"
    password_id="pcPassword"
    login_btn_id="loginBtn"
    system_tools_menu_id="menu_tools"
    reboot_menu_id="menu_restart"
    reboot_btn_id="button_reboot"


    #locateids
    login_feild_user=driver.find_element(By.ID, user_id)
    login_feild_pass=driver.find_element(By.ID, password_id)
    login_btn=driver.find_element(By.ID,login_btn_id)
    
    #fill
    # login_feild_user.send_keys(username) 
    login_feild_pass.send_keys(password)

    #automation
    login_btn.click()
    driver.switch_to.frame("frame1")
    menu_btn=driver.find_element(By.ID,system_tools_menu_id)
    menu_btn.click()
    menu_restart=driver.find_element(By.ID,reboot_menu_id)
    menu_restart.click()
    driver.switch_to.parent_frame()
    driver.switch_to.frame("frame2")
    reboot_btn=driver.find_element(By.ID,reboot_btn_id)
    reboot_btn.click()
    alart=driver.switch_to.alert
    alart.accept()
    print("Rebooting sucessfully")


my_tplink()