from logging import exception
from selenium import webdriver
import time
import sys


options = webdriver.ChromeOptions()
options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(chrome_options=options, executable_path="C:/Utility/BrowserDrivers/chromedriver.exe")

driver.get('https://www.instagram.com/p/B166OkVBPJR/')
time.sleep(3)

#if user not logined
try:
    close_button = driver.find_element_by_class_name('xqRnw')
    close_button.click()
except:
    pass


try:
    load = driver.find_element_by_class_name('dCJp8')
    i = 0
    while load.is_displayed:
        i = i + 1
        print(i)
        load.click()
except Exception as e:
    print(e)
    pass

try:
    load_more_comment = driver.find_element_by_css_selector('.EizgU')
    print("Found {}".format(str(load_more_comment)))
    i = 0
    while load_more_comment.is_displayed() and i < int(5):
        load_more_comment.click()
        time.sleep(1.5)
        load_more_comment = driver.find_element_by_css_selector('.EizgU')
        print("Found {}".format(str(load_more_comment)))
        i += 1
except Exception as e:
    print(e)
    pass

user_names = []
user_comments = []
comment = driver.find_elements_by_class_name('Mr508  ')

for c in comment:
    container = c.find_element_by_class_name('C4VMK')
    name = container.find_element_by_class_name('_6lAjh').text
    content = container.find_element_by_tag_name('span').text
    content = content.replace('\n', ' ').strip().rstrip()
    print(content)
    user_names.append(name)
    user_comments.append(content)

user_names.pop(0)
user_comments.pop(0)


driver.close()