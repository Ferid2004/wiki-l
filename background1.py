from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_body_background_color():

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)


    url = "https://en.wikipedia.org/wiki/NASA"
    driver.get(url)

    try:

        body_element = driver.find_element("tag name", "body")
        background_color = body_element.value_of_css_property("background-color")

        # RGB formatından hex formata çevir
        def rgb_to_hex(rgb):
            return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

        bg_color = background_color.split('(')[1].split(')')[0].split(',')
        bg_color = tuple(int(c.strip()) for c in bg_color[:3])
        hex_color = rgb_to_hex(bg_color)


        if hex_color == "#000000":
            print("Body elementinin arka plan rengi #000000 (siyah).")
        else:
            print(f"Body elementinin arka plan rengi {hex_color}.")

    except Exception as e:
        print("Bir hata oluştu:", e)
    
    finally:

        driver.quit()


test_body_background_color()