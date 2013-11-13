#!/usr/bin/python

import urllib2
import sys
from bs4 import BeautifulSoup
import re

#Asks user what sport score they want to see
def getUserPreference():
	pref = raw_input("For what sport would you like to see the score for? (nba, nfl, etc): ")
	pref = "http://sports.yahoo.com/" + pref + "/scoreboard/"
	return pref

#Gets the html format of yahoo's scoreboard
def getHTML( website ):
	
	webRequest = urllib2.Request(website)
	response   = urllib2.urlopen(webRequest)
	htmlPage   = response.read()
	return htmlPage

#Converts HTML part of name and returns the name in string format
def getName( teamHTML ):
	name = teamHTML.find('em')
	name = str(name)
	name = name.replace("<em>", "")
	name = name.replace("</em>", "")
	return name

#Converts HTML part of score and returns the score in string format
def getScore( scoreHTML ):
	scoreHTML = str(scoreHTML)
	scoreHTML = re.sub('<[^>]+>', '', scoreHTML)
	return scoreHTML

#Runs main program, gets team name and score
def getData( HTMLpage):
	gameCheck = 0
	print "------------------------"
	parsed_html = BeautifulSoup(htmlPage)
	for scores in parsed_html.findAll('tr', attrs={'class': 'game   link'}):
		awayTeamHTML  = scores.find('td', attrs={'class': 'away'})
		awayScoreHTML = scores.find('span', attrs={'class': 'away'})
		awayTeam      = getName(awayTeamHTML)
		awayScore     = getScore(awayScoreHTML)

		homeTeamHTML  = scores.find('td', attrs={'class': 'home'})
		homeScoreHtml = scores.find('span', attrs={'class': 'home'})
		homeTeam      = getName(homeTeamHTML)
		homeScore     = getScore(homeScoreHtml)

		print awayTeam + ": " + awayScore
		print homeTeam + ": " + homeScore
		print "------------------------"
		gameCheck = 1
	
	if gameCheck == 0:
		print "No scores/games right now!"
		print "------------------------"


#Main program
sport = getUserPreference()
htmlPage = getHTML(sport)
getData(htmlPage)
