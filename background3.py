from selenium import webdriver
import time


driver_path = 'path_to_webdriver/msedgedriver.exe' 
driver = webdriver.Edge(executable_path=driver_path)

driver.get('https://www.wikipedia.org/')
script = "document.body.style.backgroundColor = '#202122';"
driver.execute_script(script)
time.sleep(5)  
driver.get('https://www.nasa.gov/')
driver.execute_script(script)
time.sleep(5)  


driver.quit()
