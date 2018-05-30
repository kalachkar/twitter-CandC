#! /usr/bin/python3

import os, requests, re, time, daemon
from bs4 import BeautifulSoup
from config import *

# check whether the string can be encoded only with ASCII characters
def isEnglish(t):
    try:
        t.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


def parser():
	while True:
	    page_link = 'https://trends24.in/' + countryName + '/'
	    page_response = requests.get(page_link, timeout=5)
	    page_content = BeautifulSoup(page_response.content, "html.parser")
	    trendTag = page_content.find_all(class_='trend-card__list')

	    #Regular expression to remove HTML tags: <[^>]*>
	    trends = (trendTag[timeInterval].get_text(',', strip=True)).split(',')

	    # get a clean list for only trends with english language
	    allTrends = [x for x in trends if isEnglish(x)]

	    print(allTrends)
	    with open('trends.txt', 'w') as f:
	        for trend in allTrends:
	            f.write("%s\n" % trend)
	    time.sleep(5)


#daemonize the script
if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    out = open(os.devnull, 'w')
    with daemon.DaemonContext(working_directory=here, stdout=out):
        print("starting regular parser daemon")
        parser()
    print("exiting")
