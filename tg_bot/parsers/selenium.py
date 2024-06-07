import undetected_chromedriver as uc
from undetected_chromedriver import By
driver = None

def run_selenium(article):
    global driver
    def login():
        global driver
        driver = uc.Chrome()
        driver.get(f'https://ozon.ru/context/detail/id/{article}/')
        try:
            while f"https://ozon.ru/context/detail/id/{article}/" in driver.current_url:
                if driver.title.lower() == "доступ ограничен":
                    driver.quit()
                    return ["None", "None", "None"]
                continue
            el = driver.find_element(By.XPATH, "//*[contains(text(), 'c Ozon Картой')]")
            previous_sibling = el.find_element(By.XPATH, "preceding-sibling::*[1]")
            curr = previous_sibling.find_element(By.CSS_SELECTOR, "*")
            txt = curr.text
            el1 = driver.find_element(By.XPATH, "//*[contains(text(), 'без Ozon Карты')]")
            par = el1.find_element(By.XPATH, "..")
            previous_sibling1 = par.find_element(By.XPATH, "preceding-sibling::*[1]")
            curr1 = previous_sibling1.find_element(By.CSS_SELECTOR, "*")
            try:
                image = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[4]/div[3]/div[1]/div[1]/div[1]/div/div/div/div/div/div[2]/div[1]/div/img")
                src = image.get_attribute("src")
            except:
                src = False
            txt1 = curr1.text
            driver.quit()
            return [txt, txt1, src]
        except:
            driver.quit()
            return ["None", "None", "None"]
    return login()

