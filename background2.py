from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def test_body_background_color():

    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)


    url = "https://en.wikipedia.org/wiki/NASA"
    driver.get(url)

    try:

        body_element = driver.find_element("tag name", "body")
        background_color = body_element.value_of_css_property("background-color")

        def rgb_to_hex(r, g, b):
            return '#{:02x}{:02x}{:02x}'.format(r, g, b)

        if 'rgba' in background_color:
            bg_color = background_color.split('(')[1].split(')')[0].split(',')
            r, g, b, _ = [int(x.strip()) for x in bg_color]
        elif 'rgb' in background_color:
            bg_color = background_color.split('(')[1].split(')')[0].split(',')
            r, g, b = [int(x.strip()) for x in bg_color]
        else:
            raise ValueError(f"Unexpected color format: {background_color}")

        hex_color = rgb_to_hex(r, g, b)


        if hex_color == "#000000":
            print("Body elementinin arka plan rengi #000000 (siyah).")
        else:
            print(f"Body elementinin arka plan rengi {hex_color}.")

    except Exception as e:
        print("Bir hata oluştu:", e)
    
    finally:

        driver.quit()


test_body_background_color()