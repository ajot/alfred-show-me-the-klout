#! /usr/bin/python

from encodings import hex_codec
from encodings import ascii
import httplib,urllib2
import json
import sys
import get_twitter_details

# Get your Klout API Key from http://developer.klout.com
klout_key = "your_klout_api_key"

def print_stuff(klout_score):
	name,friends_count,followers_count,ff_ratio,created_at = get_twitter_details.get_details(twitter_handle)
	
	print "%s:\r\r" % (name)
	print "Follows: %s \r" % (friends_count)
	print "Followers: %s  \r\r--\r\r" % (followers_count)	
	print "Klout Score: %s \r" % (klout_score)
	print "Follow vs Followers Ratio: %s \r\r" % (ff_ratio)
	print "Joined Twitter on: %s" % (created_at).strftime('%a, %d %h %Y')


#getting user input
if len(sys.argv) < 2:
    sys.exit(2) #if no argument is provided, exit the program

#Assigning the user input to a variable twitter_handle
twitter_handle = sys.argv[1]

try:
	#Accessing Klout API to get the Klout ID using the Twitter handle
	url = "http://api.klout.com/v2/identity.json/twitter?screenName=%s&key=%s" % (twitter_handle, klout_key)
	json = urllib2.urlopen(url).read()
	
	# convert to a native python object
	(true,false,null) = (True,False,None)
	
	#Parsing the json payload
	klout_id_data = eval(json)
	
	#Retrieving klout_id from the payload
	klout_id = klout_id_data ['id']

	#Accessing Klout API to get the Klout score using the KloutID
	url = "http://api.klout.com/v2/user.json/%s?key=%s" % (klout_id, klout_key)
	json = urllib2.urlopen(url).read()

	# convert to a native python object
	(true,false,null) = (True,False,None)
	klout_score_data = eval(json)
	
	#Retrieving klout_id from the payload
	klout_score = klout_score_data ['score']['score']

	klout_score = str(round(klout_score))
	print_stuff(klout_score)
	
except urllib2.URLError, e:
    if hasattr(e, 'reason'):
        print 'We failed to reach a server.\r'
        print 'Reason: ', e.reason
    elif hasattr(e, 'code'):
        print 'Sorry! Looks like Klout doesn\'t have info on that soldier!\r'
        print 'Error code: ', e.code