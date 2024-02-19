from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#to catch the page source if needed.
def catch(html):
    with open("page1.html","w", encoding="utf-8") as x:
        x.write(html)
        
def my_tplink():
    option=Options()
    option.add_argument("-headless")
    driver=webdriver.Chrome(options=option)

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

def digisol():
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
    print('Process digisol Complete!')


def temp():
    print("Will replace this code with parent router of home tp link")

if __name__=="__main__":
    func ={'0':my_tplink,'1':temp,'2':digisol}
    userInp=input("""
                  enter '0' for home
                  enter '1' for home_parent
                  enter '2' for office
                  =>
                  """)
    func[userInp]()

