from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\MohammadDaimi\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.amazon.in/")

driver.find_element_by_partial_link_text("Sellers").click()
driver.find_element_by_link_text("Books").click()

driver.quit()