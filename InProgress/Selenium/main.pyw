import time
from selenium import webdriver

driver = webdriver.Chrome('C:\Program Files (x86)\Python37-32\chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml');
# time.sleep(1) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('Hello')
search_box.submit()
time.sleep(10) # Let the user actually see something!
driver.quit()