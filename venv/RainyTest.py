from selenium import webdriver
import time

#------------------Function definition--------------------------------------------------------------
def validate_Pagelement(exp_val,act_val):
    if (exp_val == act_val):
        print("Match found!!! Expected value is %S and the actual value is %S" % (exp_val, act_val))
    else:
        print("No Match found!!! Expected value is %S and the actual value is %S" % (exp_val, act_val))
#------------------------------------------------------------------------------------------------------

#--------------TestScript------------------------------------------------------------------------------
#1. Launch Chrome browser
driver = webdriver.Chrome("G:\educational\softwares\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

#2. Navigate to the URL: https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

'''3. Enter Username and password in the respective fields. 
        Email : admin@yourstore.com
        Password : admin'''
driver.find_element_by_id("Email").clear()
driver.find_element_by_id("Email").send_keys("admin@yourstore.com")
driver.find_element_by_id("Password").clear()
driver.find_element_by_id("Password").send_keys("admin")

#4. Click on Login button
driver.find_element_by_xpath("//button[@class='button-1 login-button']").click()

#5. Validate the title value and it should match "Dashboard / nopCommerce administration"
expTitle_val = "Dashboard / nopCommerce administration"
actTitle_val = driver.title
validate_Pagelement(expTitle_val,actTitle_val)

#6. Print the name of the user (top right corner - John Smith  00252)
expUser_val = "John Smith"
actUser_val = driver.find_element_by_xpath("//a[@class='nav-link disabled']").text
validate_Pagelement(expUser_val,actUser_val)

#7. click on the Logout button and it should logout but compare the title as Your store. Login
driver.find_element_by_xpath("//a[@href='/logout']").click()
print(driver.title)

time.sleep(10)
driver.quit()

