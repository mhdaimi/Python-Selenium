from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\MohammadDaimi\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")

driver.find_element_by_css_selector("input[id='isAgeSelected']").click()

all_checkboxes = driver.find_elements_by_css_selector("input[class='cb1-element']")


for i in range(0,len(all_checkboxes),2):
    all_checkboxes[i].click()
    
driver.quit()