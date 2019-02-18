import time
from selenium import webdriver

driver = webdriver.Chrome('C:\Program Files (x86)\Python37-32\chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml');
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('https://accounts.google.com')
# search_box.submit()
driver.get("https://accounts.google.com");
name_box = driver.findElement(By.cssSelector("input"))
name_box.send_keys('nitheeshmsk')
name_box.submit()

time.sleep(10) # Let the user actually see something!
driver.quit()