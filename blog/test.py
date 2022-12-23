from selenium import webdriver
import time

driver= webdriver.Chrome()
driver.get(url="http://bioly1910.pythonanywhere.com/admin")

def element_is_clickable():
    driver.find_element_by_xpath('//*[@id="id_username"]').send_keys("bioly1910")
    driver.find_element_by_xpath('//*[@id="id_password"]').send_keys("grabarzmichal1910")
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="user-tools"]/a[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/nav/div/a/span').click()

element_is_clickable()

driver.get(url="http://bioly1910.pythonanywhere.com")

def response_check(w, file):            # funkcja do sprawdzenia responywności strony (zachowania w różnych roździelczościach - zbadamy zachowanie parametrem w [width - szerokość])
    height = 768
    driver.set_window_size(w, height)   # ustawiamy wysokość strony
    driver.save_screenshot(file)

response_check(900, "test900.png")      #(w=900, file="test900.png")
response_check(1200, "test1200.png")
response_check(1800, "test1800.png")
response_check(600, "test600.png")




driver.close()