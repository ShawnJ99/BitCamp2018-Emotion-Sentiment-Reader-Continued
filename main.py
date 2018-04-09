#!/usr/bin/python
import functions
import Tweet
import parser
import os
import sys

# This is the main driver method.
# It takes 2 arguments:
#	- One twitter handle (without the @)
#	- An integer value greater than 0 for the number of tweets to be read

def main():
	nTweets = 50
	if (len(sys.argv) == 3 and sys.argv[2] > 0):
		nTweets = ((int) (sys.argv[2])) + 1

	data = parser.getTweets(sys.argv[1], nTweets)
	functions.printMentionHashtagSentiment(data)

if __name__== "__main__":
  main()