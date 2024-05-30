from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver_path = 'path_to_webdriver/msedgedriver.exe'  # EdgeDriver'ın yolunu belirtin
driver = webdriver.Edge(executable_path=driver_path)


driver.get('https://www.wikipedia.org/')


driver.get('https://www.nasa.gov/')


driver.get('https://www.nasa.gov/sites/default/files/atoms/files/fy_2021_nasa_budget_highlights.pdf') 


script = """
var tables = document.getElementsByTagName('table');
for (var i = 0; i < tables.length; i++) {
    tables[i].style.boxSizing = 'border-box';
}
"""
driver.execute_script(script)

time.sleep(5)


driver.quit()
