from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import asyncio
import time

for i in range(64,73):
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



# def main():
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
    
#     result = loop.run_until_complete(get_episode_text(index))
    

# async def get_episode_text(index):
#     # i = index
#     # my_url = "https://complexity.simplecast.com/episodes/"+str(i)+"/transcript"
#     await driver.get(my_url)
#     transcript = driver.find_element_by_class_name("sc-episode-details-body")
#     return transcript