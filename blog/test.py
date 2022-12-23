from selenium import webdriver
import time

driver= webdriver.Chrome()
driver.get(url="http://bioly1910.pythonanywhere.com/admin")

def element_is_clickable():
    driver.find_element_by_xpath('//*[@id="id_username"]').send_keys("bioly1910")
    driver.find_element_by_xpath('//*[@id="id_password"]').send_keys("grabarzmichal1910")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()

element_is_clickable()   
driver.close()