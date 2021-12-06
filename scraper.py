import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'
response = requests.get(YOUTUBE_TRENDING_URL)

with open('trending.html', 'w' ) as f :
  f.write(response.text)

doc = BeautifulSoup(response.text, 'html.parser')
print('Page title : ', doc.title.text)

#Find all the video divs
video_divs = doc.find_all('div', class_ = 'ytd-video-renderer')
print(len(video_divs))

driver = webdriver.Chrome()
driver.gwt(YOUTUBE_TRENDING_URL)