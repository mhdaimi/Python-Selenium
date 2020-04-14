from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\MohammadDaimi\chromedriver_win32\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")

print(driver.title)

driver.close()