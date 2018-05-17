#! /usr/bin/python3

import requests, re
from bs4 import BeautifulSoup



# check whether the string can be encoded only with ASCII characters
def isEnglish(t):
    try:
        t.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


def main():
	timeInterval = 1 #Pick the time interval from trends24 e.g. ( 0 current hour, 1 past one hour and so on)
	countryName = 'netherlands' #choose the country e.g. (united-kingdom, netherlands) or keep it empty for world wild
	page_link = 'https://trends24.in/' + countryName + '/'
	page_response = requests.get(page_link, timeout=5)
	page_content = BeautifulSoup(page_response.content, "html.parser")
	trendTag = page_content.find_all(class_='trend-card__list')

	#Regular expression to remove HTML tags: <[^>]*>
	trends = (trendTag[timeInterval].get_text(',', strip=True)).split(',')

	# get a clean list for only trends with english language
	allTrends = [x for x in trends if isEnglish(x)]

	print(allTrends)
	f = open('trends.txt', 'w')
	for trend in allTrends:
	  f.write("%s\n" % trend)


#call main function
main()

