import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    service = Service("chromedriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def wait(driver):
    return WebDriverWait(driver, 10)

def test_logo_size(driver, wait):
    driver.get("https://en.wikipedia.org/wiki/NASA")
    eleLogo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.mw-wiki-logo')))
    assert eleLogo.size['width'] == 160
    assert eleLogo.size['height'] == 160