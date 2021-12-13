from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import asyncio
import time

for i in range(4,5):
    driver = webdriver.Safari()

    my_url = "https://complexity.simplecast.com/episodes/"+str(i)+"/transcript"
    driver.get(my_url)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "sc-episode-details-body"))
        )
        with open(str(i)+".md","w") as f:
            f.write(element.text)
    finally:
        driver.quit()
    
    time.sleep(2)