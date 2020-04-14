from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\MohammadDaimi\chromedriver_win32\chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/input-form-demo.html")

driver.find_element_by_name("first_name").send_keys("Sonam")
driver.find_element_by_name("last_name").send_keys("Gupta")
driver.find_element_by_name("email").send_keys("bewafasonam@gmail.com")
driver.find_element_by_name("phone").send_keys("8404204200")
driver.find_element_by_name("address").send_keys("Gupta nagar, sonam vihar, Delhi-420")
driver.find_element_by_name("city").send_keys("New Delhi")
driver.find_element_by_name("zip").send_keys("420420")
driver.find_element_by_name("website").send_keys("www.sonambewafa.com")
driver.find_element_by_name("hosting").click()
driver.find_element_by_name("comment").send_keys("This is a demo project!")
driver.find_element_by_xpath("//button[contains(text(), 'Send ')]").click()

driver.quit()