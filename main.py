from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class Tplink_Archer_C20:
    def __init__(self,gateway,username,password):
        self.geteway=f"http://{gateway}/"
        self.username=username
        self.password=password
    user_id="userName"
    password_id="pcPassword"
    login_btn_id="loginBtn"
    system_tools_menu_id="menu_tools"
    reboot_menu_id="menu_restart"
    reboot_btn_id="button_reboot"


def catch(html):
    with open("page1.html","w", encoding="utf-8") as x:
        x.write(html)
        
def my_tplink():
    option=Options()
    option.add_argument("-headless")
    driver=webdriver.Chrome(options=option)

    tplink_home=Tplink_Archer_C20(gateway="192.168.0.3",username="admin",password="admin123")
    #loadpage
    driver.get(tplink_home.geteway)
    driver.implicitly_wait(10)

    try:
        userName=driver.find_element(By.ID, tplink_home.user_id)
        userName.send_keys(tplink_home.username)
    except Exception as e:
        print("username Exception! Trying to reboot.")
    passWord=driver.find_element(By.ID, tplink_home.password_id)
    passWord.send_keys(tplink_home.password)
    loginBtn=driver.find_element(By.ID,tplink_home.login_btn_id)
    loginBtn.click()
    print("Login sucessful")
    
    driver.switch_to.frame("frame1")
    menu_btn=driver.find_element(By.ID,tplink_home.system_tools_menu_id)
    menu_btn.click()
    menu_restart=driver.find_element(By.ID,tplink_home.reboot_menu_id)
    menu_restart.click()
    driver.switch_to.parent_frame()
    driver.switch_to.frame("frame2")
    reboot_btn=driver.find_element(By.ID,tplink_home.reboot_btn_id)
    reboot_btn.click()
    alart=driver.switch_to.alert
    alart.accept()
    print("Rebooting")


def parent_tplink():
    username="admin"
    password="password"
    router=Tplink_Archer_C20(gateway="192.168.0.1",username="admin",password="admin")
    
    #headlessmode
    options=Options()
    options.add_argument("-headless") 
    driver=webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get(router.geteway)
    
    #input feild
    try:
        userName=driver.find_element(By.ID,router.user_id)
        userName.send_keys(username)
        pcPassword=driver.find_element(By.ID,router.password_id)
        pcPassword.send_keys(password)
        loginBtn=driver.find_element(By.ID,router.login_btn_id)
        loginBtn.click()
        print("Logged in.")
    except Exception as e:
        print(e)
    # frame1
    driver.switch_to.frame('frame1')
    system_tools=driver.find_element(By.ID,router.system_tools_menu_id)
    system_tools.click()
    reboot_menu=driver.find_element(By.ID,router.reboot_menu_id)
    reboot_menu.click()
    driver.switch_to.parent_frame()
    
    #frame2
    driver.switch_to.frame('frame2')
    reboot_btn=driver.find_element(By.ID,router.reboot_btn_id)
    reboot_btn.click()
    
    #alart
    reboot_alart=driver.switch_to.alert
    reboot_alart.accept()
    print("Rebooting")
    
    

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


if __name__=="__main__":
    func ={'0':my_tplink,'1':parent_tplink,'2':digisol}
    userInp=input("""
                  enter '0' for home
                  enter '1' for home_parent
                  enter '2' for office
                  =>
                  """)
    func[userInp]()

