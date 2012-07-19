from __future__ import division
import twitter_auth #calling the Twitter auth module

def get_details(twitter_handle):
	# Get the User object for twitter...
	user = twitter_auth.api.get_user(twitter_handle)

	#Calculating the followers vs following ratio
	ff_ratio = round(int(user.followers_count) / int(user.friends_count),2)

	#Returning Twitter details as a Tuple
	return (user.name,user.friends_count,user.followers_count,ff_ratio,user.created_at)