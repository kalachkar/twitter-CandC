#pip all requirments + twint + tweepy
#To-Do: add instructions from here: https://github.com/haccer/twint and https://github.com/tweepy/tweepy
import tweepy, json, twitter, twint
from credentials import *

#User credintials
'''
CONSUMER_KEY = 'xyz'
CONSUMER_SECRET = 'xyz'
ACCESS_KEY = 'xyz'
ACCESS_SECRET = 'xyz'
'''

#Locations Dictionary
#if you need to add more locations, check this repository: https://gist.github.com/edsu/a5f6c1188ec3a27d38634721fb25fffb
locationsDic = {
		"Worldwide" : 1,
		"Canada" : 23424775,
		"United Kingdom" : 23424975,
		"Dominican Republic" : 23424800,
		"Guatemala" : 23424834,
		"Mexico" : 23424900,
		"Argentina" : 23424747,
		"Chile" : 23424782,
		"Colombia" : 23424787,
		"France" : 23424819,
		"Ecuador" : 23424801,
		"Germany" : 23424829,
		"Italy" : 23424853,
		"Netherlands" : 23424909,
		"Spain" : 23424950,
		"Switzerland" : 23424957,
		"Latvia" : 23424874,
		"Norway" : 23424910,
		"Sweden" : 23424954,
		"Ukraine" : 23424976,
		"Greece" : 23424833,
		"Australia" : 23424748,
		"Japan" : 23424856
	}

#Get trends based on specific location
#User credintials are imported from a seperate credentials.py file. You can also define these variables explicitly as shown above
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

trendsList = api.trends_place(locationsDic["Netherlands"]) # from the end of your code
# trendsList is a list with only one element in it, which is a 
# dict which we'll put in data.
data = trendsList[0] 
# grab the trends
trends = data['trends']
# grab the name from each trend
names = [trend['name'] for trend in trends]
# put all the names together with a ' ' separating them

print("\n\nTrends are:")
trendsName = "*".join(names)
#print(trendsName.encode("utf-8"))
#print("bye")
#print(len(trendsName))
#final = str(trendsName.encode("utf-8")).replace("*", "\n")

#get a clean list of all trends in a array
allTrends = []
allTrends = str(trendsName.encode("utf-8")).split("*")
#Get ride of the Bytes literals that is always prefixed with 'b'
allTrends[0] = allTrends[0].replace('b\'', '', 1) 
allTrends[len(allTrends) - 1] = allTrends[len(allTrends) - 1][:-1]

#Print a clean list of all trends
print(allTrends)


# get all tweets for a specific user (also using a specific hashtags)
c = twint.Config()
c.Username = "delgado_ahmed"
#c.Search = allTrends[0] #Seach for specific hashtag name. In this case it used the trending list to fetsh for that specific hashtag. you can also search for multiple hashtags using advance query
c.Format = "{tweet}" #"username: {username} | hashtags: {hashtags} | location: {location} | Tweet id: {id} | Tweet: {tweet}"
# Run
twint.Search(c)

