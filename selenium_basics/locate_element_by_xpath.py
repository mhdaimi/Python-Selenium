from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\MohammadDaimi\chromedriver_win32\chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")

driver.find_element_by_xpath("//input[@type='radio' and @value='Male']").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@value='Female' and @name='gender']").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@value='15 - 50' and @name='ageGroup']").click()
time.sleep(2)
driver.quit()