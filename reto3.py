from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys

options = webdriver.ChromeOptions()
options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
options.add_argument("--disable-infobars")
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
options.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})
driver = webdriver.Chrome(chrome_options=options, executable_path="C:/Utility/BrowserDrivers/chromedriver.exe")




driver.get('https://www.facebook.com')
email = driver.find_element_by_name('email')
email.send_keys(sys.argv[1])
password = driver.find_element_by_id('pass')
password.click()
password.send_keys(sys.argv[2])
login = driver.find_element_by_name('login')
login.click()
logout = driver.find_element_by_class_name('d2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.lr9zc1uh.a8c37x1j.keod5gw0.nxhoafnm.aigsh9s9.d3f4x2em.fe6kdd0r.mau55g9w.c8b282yb.iv3no6db.jq4qci2q.a3bd9o3v.ekzkrbhg.oo9gr5id.hzawbc8m')

driver.get(sys.argv[3])

like = driver.find_element_by_class_name('gpro0wi8.cwj9ozl2.bzsjyuwj.ja2t1vim')



like.click()    
scroll = driver.find_element_by_class_name('j83agx80.cbu4d94t.buofh1pr.l9j0dhe7')
print(scroll)
driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scroll)


time.sleep(4)
invites = driver.find_elements_by_xpath("//span[contains(text() ,'Invitar')]")
print(invites)
for i in invites:
    print(i.text)
    i.click()
time.sleep(3)