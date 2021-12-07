import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd 


YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'
response = requests.get(YOUTUBE_TRENDING_URL)

def get_videos(driver):
  driver.get(YOUTUBE_TRENDING_URL)
  video_divs = driver.find_elements(By.TAG_NAME,'ytd-video-renderer') 
  return video_divs
def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def parse_video(video):
  title_tag = video.find_element(By.ID, 'video-title')
  title = title_tag.text
  url = title_tag.get_attribute('href')
  thumbnail_url = video.find_element(By.TAG_NAME, 'img').get_attribute('src')
  channel_name = video.find_element(By.CLASS_NAME, 'ytd-channel-name').text
  description = video.find_element(By.ID, 'description-text').text
  return {
    'title':title,
    'url': url,
    'thumbnail_url': thumbnail_url,
    'channel' : channel_name,
    'description': description
  }
if __name__ == '__main__':
  print('Creating Driver')
  driver = get_driver()

  print('Fetching the page')
  driver.get(YOUTUBE_TRENDING_URL)

  print('Fetching Trending Videos')
  videos = get_videos(driver)

  print(f'Found {len(videos)} Videos')

  print('Parsing Top 10 videos')

  videos_data = [parse_video(video) for video in videos[:10]]

  videos_df = pd.DataFrame(videos_data)
  print(videos_df)
  videos_df.to_csv('trending.csv')

