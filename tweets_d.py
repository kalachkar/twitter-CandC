#! /usr/bin/python3

import tweepy, twitter, json, twint, requests, re, time, os, sys, subprocess, string
from descriptionToValue import *

# Get Today's date
TODAY = time.strftime("%Y-%m-%d")
OLD_COMMAND = ''

#List of commands
commandsList = {'echo \'The guy with this ip-address: <IP-ADDRESS> is a Legend! Just a Legend !!\' | telegram-send --stdin',
 				'dig <IP-ADDRESS> | telegram-send --stdin',
                'nslookup <IP-ADDRESS> | telegram-send --stdin'}

#Check whether the tweet is a command or not (check whether it contains double spaces after or not)
def isCommand(tweet, OLD_COMMAND):
    return True if tweet.count('  ') > 0 and tweet != OLD_COMMAND else False 

#get all trends from trends.txt as a list
def getTrends():
	with open('trends.txt', 'r') as f:
		t = f.read().strip().split('\n')
		f.close()
	return t

#Clean the output file every time we make the call
def fileCleaner():
	f= open("tweets.txt","w+")
	f.write('')
	f.close()
	
def getTweets():	
	trendsList = getTrends()
	searchQuery = trendsList[0] + " OR " + trendsList[1] + " OR " + trendsList[2]
	c = twint.Config()
	c.Username = "delgado_ahmed"
	#c.Search = searchQuery  # AND ,OR, NOT query to search for trends
	c.Format = "{tweet}"
	c.Since = TODAY  # Specify the tweet time (today)
	c.Output = "tweets.txt"
	fileCleaner()
	twint.Search(c)

def emojiToIP(tweet, dic):
	lss = re.findall('<.*>', tweet)
	s = str(lss[0]).replace('>', '>,')
	emojiIP = s.split(",")
	ipAddress = str(dic[emojiIP[0]] + dic[emojiIP[1]]) + "." + str(dic[emojiIP[2]] + dic[emojiIP[3]]) + "." + str(dic[emojiIP[4]] + dic[emojiIP[5]]) + "." + str(dic[emojiIP[6]] + dic[emojiIP[7]])
	
	return ipAddress 
	
def commander():
	lastTweet = ''
	x = ''
	try:
		with open('tweets.txt') as f:
			lastTweet = f.readline()  # get only the last tweet
		x = emojiToIP(lastTweet, dic1)
	except FileNotFoundError:
		print("tweets.txt file not found")

	return x

def main():
	trends = getTrends()
	getTweets()
	print(commander())

main()
	

#os.stat("tweets.txt").st_size == 0