#! /usr/bin/python3

import tweepy, twitter, json, twint, requests, re, time, os, sys, subprocess, string, time
from descriptionToValue import *

# Get Today's date
TODAY = time.strftime("%Y-%m-%d")

#List of commands
commandsList = {1 : 'echo \'This IP address (<IP-ADDRESS>) getting DOS for REAL!\' | telegram-send --stdin',
 				2 : 'dig <IP-ADDRESS> | telegram-send --stdin',
                3 : 'nslookup <IP-ADDRESS> | telegram-send --stdin'}


def findOccurences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


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
	emojiIP = []
	endChars = findOccurences(tweet, '>')
	for i, startChar in enumerate(findOccurences(tweet, '<')): emojiIP.append(tweet[startChar:endChars[i]+1])
	#s = lss.replace(">",">,").split(",")
	#emojiIP = s.split(",")
	ipAddress = str(dic[emojiIP[0]] + dic[emojiIP[1]]) + "." + str(dic[emojiIP[2]] + dic[emojiIP[3]]) + "." + str(dic[emojiIP[4]] + dic[emojiIP[5]]) + "." + str(dic[emojiIP[6]] + dic[emojiIP[7]])
	
	return ipAddress 
	
def commander(dic):
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
	OLD_COMMAND = ''

	#daemonize the script
	while True:
		trends = getTrends()
		print(trends)
		getTweets()
		com = ''
		if(os.stat("tweets.txt").st_size != 0):
			with open('tweets.txt') as f:
				lastTweet = f.readline()  # get only the last tweet
				print("zzzz", lastTweet)
				
				if(isCommand(lastTweet,OLD_COMMAND)):
					
					OLD_COMMAND = lastTweet
					
					if(trends[0] in lastTweet):
						ip = emojiToIP(lastTweet, dic1)
						com = commandsList[1].replace("<IP-ADDRESS>", ip)
						print(com, " has been successfully executed !!")
					elif(trends[1] in lastTweet):
						ip = emojiToIP(lastTweet, dic2)
						com = commandsList[2].replace("<IP-ADDRESS>", ip)
						print(com, " has been successfully executed !!")
					elif(trends[2] in lastTweet):
						ip = emojiToIP(lastTweet, dic3)
						com = commandsList[3].replace("<IP-ADDRESS>", ip)
						print(com, " has been successfully executed !!")
					else:
						print("Command called not in the list")
				
				else:
					print("No command has been called yet!!")
			os.system(com)
		else:
			print("No tweets for today")
		#Specify the delay in seconds between every round
		time.sleep(60)
		
main()
	

#os.stat("tweets.txt").st_size == 0