import time


def scroll_to_page_end(driver):
    old_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, arguments[0]);", old_scroll_height)
        time.sleep(2)
        new_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
        if old_scroll_height == new_scroll_height:
            break
        old_scroll_height = new_scroll_height


def extract_videos_data(soup):
    video_elements = soup.find_all('ytd-rich-item-renderer')
    videos_data = []

    for videos in video_elements:
        title = videos.find("yt-formatted-string", {"id": "video-title"}).text
        views = videos.find('span', {"class": "inline-metadata-item style-scope ytd-video-meta-block"}).text
        video_duration = videos.find('span', {"class": "style-scope ytd-thumbnail-overlay-time-status-renderer"}).text.strip()
        uploaded_at = videos.find('div', {"class": "style-scope ytd-video-meta-block"}).text.strip().split('\n')[-1::-3][0]
        thumbnail = videos.find('img', {"style": "background-color: transparent;"}).get('src')

        video_data = {
            "Title": title,
            "Views": views,
            "Video Duration": video_duration,
            "Uploaded_at": uploaded_at,
            "Thumbnail": thumbnail
        }
        videos_data.append(video_data)
    return videos_data
