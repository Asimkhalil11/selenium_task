import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/@zusmani78/videos")
time.sleep(2)

old_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(2)
    new_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")

    if old_scroll_height == new_scroll_height:
        break
    old_scroll_height = new_scroll_height

driver.quit()
