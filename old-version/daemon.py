import tweepy
import twitter
import json
import twint
import requests
import re
import time
import os
import string
from credentials import *
from emojis import emojisDic
from bs4 import BeautifulSoup

# Get Today's date
TODAY = time.strftime("%Y-%m-%d")


# check whether the string can be encoded only with ASCII characters
def isEnglish(t):
    try:
        t.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

# Check whether its a command of not by checking if there is 3 space in
# the tweet


def isCommand(tweet):
    return True if tweet.count('   ') > 0 else False

# Remove the additional zeros' while constructing the ip address


def zeroRemover(x):
    l = x.split('.')

    for i in range(0, len(l)):
        if len(l[i]) == 4:
            l[i] = l[i].replace('00', '0', 1)
        elif len(l[i]) == 5:
            l[i] = l[i].replace('00', '', 1)
    ip = '.'.join(l)

    return ip

# get a clear IP address from a tweet's emojis
#double check this (need fixes)

def toIP(z):
    lss = re.findall('<.*>', z)
    emojiIp = str(lss[0]).replace('> ', '>.')
    # print(emojiIp)
    for key, value in emojisDic.items():
        emojiIp = emojiIp.replace(key, str(value))
    return zeroRemover(emojiIp)


# Get all trends from trends24.in for a specific country
# using BeautifulSoup (bs4)
#
# Pick which table you want to work with at trends24
# specify the trend time in hours ( 0: current trends in this hour, 1: an
# hour ago, 2: two hours ago, and so on)
trendsTime = 1
# keep it empty for worldwide or specify country. such as united-kingdom,
# netherlands, and so on
countryName = 'netherlands'
pageLink = 'https://trends24.in/' + countryName + '/'
pageResponse = requests.get(pageLink, timeout=5)
pageContent = BeautifulSoup(pageResponse.content, "html.parser")
trendTag = pageContent.find_all(class_='trend-card__list')

# A Regular expression like to remove HTML tags: <[^>]*>
# print (trendTag[trendsTime].get_text(',', strip=True).encode('utf-8'))
allTrends = (trendTag[trendsTime].get_text(',', strip=True)).split(',')
# allUsableTrends = [x for x in allTrends if isEnglish(x)]
# get a clean list for only trends with hashtag and english language
hashtagTrends = [x for x in allTrends if "#" in x and isEnglish(x)]

print(hashtagTrends)

# Search query that check for each of the three most hashtaged trends using
searchQuery = hashtagTrends[0] + " OR " + \
    hashtagTrends[1] + " OR " + hashtagTrends[2]
# print(searchQuery)

# list of command to execute by substituting the <IP-Address> with the
# actual IP:
commandsList = {hashtagTrends[0]: 'echo \'The guy with this ip-address: <IP-Address> is a Legend! Just a Legend !!\' | telegram-send --stdin',
                hashtagTrends[1]: 'dig <IP-Address> | telegram-send --stdin',
                hashtagTrends[2]: 'nslookup <IP-Address> | telegram-send --stdin'}

# Get all tweets for a specific user (for a specific hashtags)
c = twint.Config()
c.Username = "delgado_ahmed"
c.Search = searchQuery  # Seach for specific hashtag name. In this case it used the trending list to fetsh for that specific hashtag. you can also search for multiple hashtags using advance query
c.Format = "{tweet}"
c.Since = TODAY  # Specify the tweet time (today)

# c.Lang = "en" #specify tweet language
c.Output = "tweets.txt"

# Run
twint.Search(c)

# After output all the tweets to a file, I only take the last one


def commander():
    com = ' '
    try:
        with open('tweets.txt') as f:
            lastTweet = f.readline()  # get only the last tweet
        if (isCommand(lastTweet)):
                # write a command for an external file to check if its used
                # later
            for i in range(0, 3):
                if hashtagTrends[i] in lastTweet:
                    com = commandsList[hashtagTrends[i]]
                    com = com.replace('<IP-Address>', toIP(lastTweet))
    except FileNotFoundError:
        print("There is no Tweets for today yet")

    return com


def main():
    if (commander() != ' '):
        print(commander())
        os.system(commander())
    else:
        print('No command has been called !!')

    # Delete file after finish
    if os.path.isfile('./tweets.txt'):
        os.remove('tweets.txt')

main()
