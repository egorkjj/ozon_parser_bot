import undetected_chromedriver as uc
from undetected_chromedriver import By

def run_selenium(article):
    with uc.Chrome() as driver:
        driver.get(f'https://ozon.ru/context/detail/id/{article}/')
        while f"https://ozon.ru/context/detail/id/{article}/" in driver.current_url:
            continue
        el = driver.find_element(By.CLASS_NAME, "lz3_27")
        return el.text
        quit()