from selenium import webdriver

#driver = webdriver.Chrome(executable_path="C:\MohammadDaimi\chromedriver_win32\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\MohammadDaimi\geckodriver-v0.26.0-win64\geckodriver.exe")
driver.get("http://newtours.demoaut.com/")

print(driver.title)

driver.close()