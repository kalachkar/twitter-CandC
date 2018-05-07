
import tweepy, twitter, json, twint, requests, re
from credentials import *
from bs4 import BeautifulSoup


# get all tweets for a specific user (also using a specific hashtags)
c = twint.Config()
c.Username = "delgado_ahmed"
c.Search = "#SACWorldSeries" #Seach for specific hashtag name. In this case it used the trending list to fetsh for that specific hashtag. you can also search for multiple hashtags using advance query
c.Format = "{tweet} | time is here {time} and date {date}"
# Run
twint.Search(c)


# Get all trends from trends24.in for a specific country
# using BeautifulSoup (bs4)
#
# Pick which table you want to work with at trends24
tableNumber = 2 # specify table ( table 1: this hour, table 2: an hour ago, and so on)
countryName = 'netherlands'

page_link = 'https://trends24.in/' + countryName + '/'
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")
trendTag = page_content.find_all(class_='trend-card__list')

#A Regular expression like to remove HTML tags: <[^>]*>
print (trendTag[tableNumber - 1].get_text(',', strip=True))
trends = (trendTag[tableNumber - 1].get_text(',', strip=True)).split(',')

