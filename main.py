from selenium import webdriver
import time

#1. Launch Chrome browser
driver = webdriver.Chrome("G:\educational\softwares\chromedriver_win32\chromedriver.exe")

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
print(driver.title)

#6. Print the name of the user (top right corner - John Smith)
print(driver.find_element_by_xpath("//a[@class='nav-link disabled']").text)

#7. click on the Logout button and it should logout but compare the title as Your store. Login
driver.find_element_by_xpath("//a[@href='/logout']").click()
print(driver.title)

time.sleep(10)
driver.quit()