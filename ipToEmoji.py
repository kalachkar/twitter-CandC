#! /usr/bin/python3

from descriptionToValue import *
from descriptionToSymbol import *
import sys


def conv(oc, dic):
	octec = int(oc)
	l = []

	if(octec >= 100 and octec < 200):
		l.append("<Emoji: Collision symbol>")
		octec -= 100
		for desc, value in dic.items():
			if value == octec:
				l.append(desc)

	elif (octec >= 200 and octec <= 255):
		l.append("<Emoji: Thumbs up sign>")
		octec -= 200
		for desc, value in dic.items():
			if value == octec:
				l.append(desc)

	else:
		l.append("<Emoji: Face with tears of joy>")
		for desc, value in dic.items():
			if value == octec:
				l.append(desc)
	return l

def toSymbol(l):
	return str(descriptionToSymbol[l[0]]) + "" + str(descriptionToSymbol[l[1]])

def main():
	
	if(len(sys.argv) >= 3):
		commandOrder = sys.argv[1] #specify the command that you want to use
		ip = sys.argv[2]
		l = ip.split(".")
		
		symbolIP = ''
		
		if(commandOrder == 1):
			dic = dic1
		elif(commandOrder == 2):
			dic = dic2
		else:
			dic = dic3
		
		for i in range(0,4):
			symbolIP += toSymbol(conv(l[i], dic))

		print(symbolIP)
	
	else:
		print("ERROR: Please run this with 2 arguments (<Trend Order> and <IP Address>)")


main()
