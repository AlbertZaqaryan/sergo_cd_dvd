from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options



def parse_data(rate):
    firefox_options = Options()
    firefox_options.add_argument("--headless")
    driver = webdriver.Firefox(options=firefox_options)
    try:
        driver.get('https://www.rate.am/hy/armenian-dram-exchange-rates/banks')
        value = driver.find_element(By.CSS_SELECTOR, f'div.group:nth-child(19) > div:nth-child({rate}) > div:nth-child(2)').text
    except Exception as ex:
        print("Error ", ex.__class__.__name__)
    finally:
        driver.close()
        driver.quit()
        return value