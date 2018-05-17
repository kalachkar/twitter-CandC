from bs4 import BeautifulSoup
import requests, re

# Pick which table you want to work with at trends24
tableNumber = 2
countryName = 'netherlands'

page_link = 'https://trends24.in/' + countryName + '/'
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")
trendTag = page_content.find_all(class_='trend-card__list')

#Regular expression to remove HTML tags: <[^>]*>
trends = (trendTag[tableNumber - 1].get_text(',', strip=True)).split(',')
print(trends)