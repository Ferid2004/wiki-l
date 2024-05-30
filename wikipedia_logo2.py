from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def test_link_styles():
  
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)


    url = "https://en.wikipedia.org/wiki/NASA"
    driver.get(url)

    try:
   
        links = driver.find_elements("tag name", "a")

        for link in links:

            font_family = link.value_of_css_property("font-family")
            font_size = link.value_of_css_property("font-size")

        
            if "sans-serif" in font_family.lower() and font_size == "12.6px":
                print("Bir bağlantının font-family'si 'Sans Serif' ve font-size'ı 12.6px.")
            else:
                print(f"Bir bağlantının font-family'si '{font_family}' ve font-size'ı '{font_size}'.")

    except Exception as e:
        print("Bir hata oluştu:", e)
    
    finally:

        driver.quit()


test_link_styles()