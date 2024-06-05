import undetected_chromedriver as uc
from undetected_chromedriver import By

driver = None

def run_selenium(article):
    global driver
    def login():
        global driver
        driver = uc.Chrome()
        driver.get(f'https://ozon.ru/context/detail/id/{article}/')
        while f"https://ozon.ru/context/detail/id/{article}/" in driver.current_url:
            continue
        el = driver.find_element(By.XPATH, "//*[contains(text(), 'c Ozon Картой')]")
        previous_sibling = el.find_element(By.XPATH, "preceding-sibling::*[1]")
        curr = previous_sibling.find_element(By.CSS_SELECTOR, "*")
        txt = curr.text
        driver.quit()
        return txt
    return login()
