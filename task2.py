from selenium import webdriver
from utils import scroll_to_page_end, extract_videos_data
from bs4 import BeautifulSoup
import pandas as pd


page_link = "https://www.youtube.com/@zusmani78/videos"
driver = webdriver.Chrome()
driver.get(page_link)
scroll_to_page_end(driver)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
data = extract_videos_data(soup)

data_frame = pd.DataFrame(data)
data_frame.to_csv('zusmani78.csv', index=False)
print("Data saved to csv file")
