from selenium import webdriver
driver = webdriver.Chrome("D:\chromedriver_win32\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/tables")

#Exercise1: Get number of rows and columns in the Example 1 webtable.

l_rows = driver.find_elements_by_xpath("//*[@id='table1']/tbody/tr")
print ("Length of rows is: " + str(len(l_rows)))

l_columns = driver.find_elements_by_xpath("//*[@id='table1']/tbody/tr[2]/td")
print ("Length of columns is: " + str(len(l_columns)))

"""Exercise2: With the reference of firstname , click on the respective edit link in the same row
              eg: if user pass the parameter value as "Frank", then the xpath should pointout the edit link the same row"""

link = driver.find_element_by_xpath("//*[@id='table1']/tbody/tr[1]/td[6]/a[1]")
print(link.text)

# Exercise3: print all the due amount in the table

due = driver.find_elements_by_xpath("//*[@id='table1']/tbody/tr/td[4]")

for dues in due:
    print(dues.text)

"""Exercise4: Get the diagonal values in the webtable
              Output:  ['Smith','Frank','jdeo@hotmail.com',$50.00]"""

for i in range(1,5):
    diag = driver.find_element_by_xpath("//*[@id='table1']/tbody/tr["+str(i)+"]/td["+str(i)+"]")
    print(diag.text)

driver.quit()
