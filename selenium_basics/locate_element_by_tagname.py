from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\MohammadDaimi\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.google.co.in/")

all_anchor_tags = driver.find_elements_by_tag_name("a")

for anchor_tag in all_anchor_tags:
    link = anchor_tag.get_attribute("href")
    link_text = anchor_tag.text # to get text of the link
    
    if "Gmail" in link_text or "Sign in" in link_text or "Images" in link_text:
        print("{} -> {}".format(link_text,link))

driver.quit()