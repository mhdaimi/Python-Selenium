from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\MohammadDaimi\chromedriver_win32\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")

print(driver.title) #print title of current page
print(driver.current_url) #print url of current page

driver.get("http://newtours.demoaut.com/mercuryregister.php") #go to another webpage
driver.maximize_window() #maximize the browser window

driver.back() #hit the browser back button

driver.refresh() #refresh current page

driver.quit() #close the browser window