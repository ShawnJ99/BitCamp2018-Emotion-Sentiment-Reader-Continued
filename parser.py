# -*- coding: UTF-8 -*-
import Tweet
import re
import csv
import tweepy
import emoji
from tweepy import OAuthHandler
from tweepy import API

# This file is the parser. It parses the data and returns it inside
# of a dictionary.


# keys and tokens from the Twitter Dev Console 						(Before committing remember to hide)
consumer_key = "f81rnWk1xGOy61lqDAQ6VQ7Ms"
consumer_secret = "aLtuyVIPugaluuPAohqngAezTOP7z7BDR4ljIR9oWcAllOD9Nl"
access_token = "179606045-AzWfFpunUf73A354XenHJbzbi4HBI6IVwWI2AVxc"
access_token_secret = "mw3czr0T295Z8CAR9GMZQipZxQfjB7uUvC6FGmpgkcNvb"

# user name is the targets twitter name
# nTweets is the n-1 tweets the user wants to view
def getTweets(username, nTweets):
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	# Gets the past 20 previous tweets
	new_tweets = api.user_timeline(screen_name=username, count=nTweets)

	tweets = []
	tweetsCSV = [tweet.text for tweet in new_tweets]
	for x in tweetsCSV:
		tweets.append((str)(emoji.demojize(x.encode('unicode_escape'))))

	dateCSV = [tweet.created_at for tweet in new_tweets] 

	allData = {} # Key =  Date, Value = tweet (Object from Tweet.py)
	for i in range(0, nTweets):
		try:
			text = re.sub(r'https:.*$', '',tweets[i])	# Removes all URLs
			text = re.sub(r'(\\[a-zA-Z0-9]+)', '', text)	# Removes all emojis
			# print "Date: {} | Text: {} | Mentions: {} | Hashtags: {}".format(dateCSV[i], text, getMentions(text), getHashTags(text))		# For testing
			allData[dateCSV[i]] = Tweet.Tweet(text, getMentions(text), getHashTags(text))
		except:
			break # If it reaches here then we have reached the end of this persons twitter page	
	return allData


def getMentions(text):
	return map(str, re.findall('(@[^-~`!@#$%^&*\(\)+=\{\}\|\][:\';\?\/.,\"<>\s]+).',text))


def getHashTags(text):
	return map(str, re.findall('(#[^-~`!@#$%^&*\(\)+=\{\}\|\][:\';\?\/.,\"<>\s]+)',text))