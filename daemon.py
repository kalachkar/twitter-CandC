import tweepy, twitter, json, twint, requests, re, time, os, string
from credentials import *
from emojis import emojisDic
from bs4 import BeautifulSoup

#Get Today's date
TODAY = time.strftime("%Y-%m-%d")

#check whether the string can be encoded only with ASCII characters
def isEnglish(t):
    try:
        t.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

#Check whether its a command of not by checking if there is 3 space in the tweet
def isCommand(tweet):
	return True if tweet.count('   ') > 0 else False

def zeroRemover(x):
	l = x.split('.')
	
	for i in range(0, len(l)):
		if len(l[i]) == 4:
			l[i] = l[i].replace('00', '0', 1)
		elif len(l[i])== 5:
			l[i] = l[i].replace('00', '', 1)
	
	ip = '.'.join(l)	
	
	return ip

#get a clear IP address from a tweet's emojis
def toIP(z):
	lss = re.findall('<.*>', z)
	emojiIp = str(lss[0]).replace('> ', '>.')
	#print(emojiIp)
	for key, value in emojisDic.items():
		emojiIp = emojiIp.replace(key, str(value))

	return zeroRemover(emojiIp)

#Make a command from a tweet: <.*>
'''def commandMaker(tweet):
	digitByDigit = list(tweet)
	c = 0
	while c < len(digitByDigit):
		if (digitByDigit[c] == '<'):

		else:
			c += 1
'''
	

# Get all trends from trends24.in for a specific country
# using BeautifulSoup (bs4)
#
# Pick which table you want to work with at trends24
trendsTime = 5 # specify the trend time in hours ( 0: current trends in this hour, 1: an hour ago, 2: two hours ago, and so on)
countryName = 'netherlands' #keep it empty for worldwide or specify country. such as united-kingdom, netherlands, and so on
pageLink = 'https://trends24.in/' + countryName + '/'
pageResponse = requests.get(pageLink, timeout=5)
pageContent = BeautifulSoup(pageResponse.content, "html.parser")
trendTag = pageContent.find_all(class_='trend-card__list')

#A Regular expression like to remove HTML tags: <[^>]*>
#print (trendTag[trendsTime].get_text(',', strip=True).encode('utf-8'))
allTrends = (trendTag[trendsTime].get_text(',', strip=True)).split(',')
#allUsableTrends = [x for x in allTrends if isEnglish(x)]
hashtagTrends = [x for x in allTrends if "#" in x and isEnglish(x)] # get a clean list for only trends with hashtag and english language

print(hashtagTrends)

#Search query that check for each of the three most hashtaged trends using
searchQuery = hashtagTrends[0] + " OR " + hashtagTrends[1] + " OR " + hashtagTrends[2]
#print(searchQuery)


# Get all tweets for a specific user (for a specific hashtags)
c = twint.Config()
c.Username = "delgado_ahmed"
c.Search =  '#weekend'  #Seach for specific hashtag name. In this case it used the trending list to fetsh for that specific hashtag. you can also search for multiple hashtags using advance query
c.Format = "{tweet}"
#c.Since = TODAY #Specify the tweet time (today)

#c.Lang = "en" #specify tweet language 
c.Output = "tweets.txt"

# Run
twint.Search(c)

#After output all the tweets to a file, I only take the last one
#FIX ME to open only if i exists
with open('tweets.txt') as f:
    lastTweet = f.readline() #get the last tweet
    os.remove('tweets.txt')


print(lastTweet)



print(toIP(z))
#run commands on server
#command = 'ping -c 4 '+ x + ' > ' + x + '.txt'
#command = 'dig ' + x + ' > ' + x + '.txt'
#command = 'nslookup ' + x + ' > ' + x + '.txt'
#print(command)
#os.system(command)



