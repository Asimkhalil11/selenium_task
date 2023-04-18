from utils import scroll_to_page_end, extract_videos_data
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


page_url = input('Please enter your YouTube URL: ')

driver = webdriver.Chrome()
# driver = webdriver.Chrome(executable_path="chromedriver")
driver.get(page_url)

scroll_to_page_end(driver)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
video_data = extract_videos_data(soup)

data_frame = pd.DataFrame(video_data)
data_frame.to_csv(f"{page_url.split('/')[-2]}.csv", index=False)

print('Extracted data save to CSV file')
