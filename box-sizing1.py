from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_budget_table_box_sizing():

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    url = "https://en.wikipedia.org/wiki/NASA"
    driver.get(url)

    try:
      
        budget_table = driver.find_element("xpath", "//table[contains(@class, 'wikitable')]")

       
        box_sizing = budget_table.value_of_css_property("box-sizing")

       
        if box_sizing == "border-box":
            print("Bütçe tablosunun box-sizing özelliği border-box'dır.")
        else:
            print(f"Bütçe tablosunun box-sizing özelliği {box_sizing}.")
    
    except Exception as e:
        print("Bir hata oluştu:", e)
    
    finally:

        driver.quit()

test_budget_table_box_sizing()