# What is "Show me the Klout"?
"Show me the Klout" is an [Alfred](http://www.alfredapp.com/) extension built using Python, that provides a quick way to know if someone is worth following on Twitter by providing critical information like their [Klout](http://klout.com) score, what's their follow vs following ratio, when did they join Twitter, number of followers, number of followings - all with a hit of a keystroke through the power of Alfred. It displays this info via a Growl notification.

## What is Alfred?
[Alfred](http://alfredapp.com) is an award-winning productivity application for Mac OS X, which aims to save you time in searching your local computer and the web. Whether it's maps, Amazon, eBay, Wikipedia, you can feed your web addiction quicker than ever.

The real power of Alfred lies in it's [powerpack](http://www.alfredapp.com/powerpack/) that allows you to create your very own Terminal shell scripts, AppleScripts, workflows, search filters and file groups to extend Alfred.

## Summary

So, you met someone new at an event or found some one interesting on the inter-webs. What's the first thing you do? Find them on Twitter. Analyze if they're worth following. How do you do that? Every time, I meet some one new, there are somethings I wanna know about them to judge if they're worth following - 

1. What's their Klout score?
2. When did they join Twitter? (It's true. I'll totally judge you on when you joined Twitter - if you were an early adopter or not. I know, am weird :)
3. What's their Follow vs Following ratio? (This is important to me. A ratio of less than 1 tells me, you're either not active on Twitter or are a spammer. Either way, probably not worth a follow.) 
4. Number of Followers
5. Number of Followings

I don't know why I do that. I just do and I do it enough to encourage me to come up with a simpler and faster process than look up people's profiles each time on Twitter.com or a Twitter client. "Show me the Klout" does just that, with just a keystroke. So, you know quickly if this person is worth a follow.

## Requirements

1. [Alfred](http://www.alfredapp.com/) + [Alfred Powerpack](http://www.alfredapp.com/powerpack/)
2. [Klout v2 API Key](http://developer.klout.com) - Make sure you get the API key for v2
3. [Twitter API Key](http://developer.twitter.com)
4. [Tweepy](http://tweepy.github.com/) - A Python library for accessing the Twitter API
5. [Growl](http://growl.info)
6. [Nice and shiny Mac](http://www.youtube.com/results?search_query=get+a+mac) - Of course you have one!

## How to Use

1. Make sure Alfred is running. 
2. Just hit your Alfred keyboard shortcut. In my case I have it configured it as **CMD + SPACE**. (The default is probably **ALT + SPACE**)

	![Alfred Launch Bar](https://github.com/mashery/alfred-show-me-the-klout/raw/master/development/images/alfred_launch_bar.png)
3. Type the keyword **ks** followed by a Twitter handle (You can change the keyword by editing the info.plist file)

	![Alfred Launch Bar](https://github.com/mashery/alfred-show-me-the-klout/raw/master/development/images/alfred_launch_bar_fill.png)	
	
4. You get a Growl notification with all the info you'd ever need to judge someone's Twitter follow worth. Enjoy!

	![Alfred Growl Notification](https://github.com/mashery/alfred-show-me-the-klout/raw/master/development/images/alfred_growl.png)

## Examples ##
	<pre>ks barackobama</pre>
	<pre>ks scobleizer</pre>

## Installation

	
1. Download the extension [here](https://github.com/mashery/alfred-show-me-the-klout/raw/master/Show%20me%20the%20Klout.zip) 

2. Double click on the .alfredextension file you just download. The extension will install and open up the preferences window in Alfred.

3. Right click on the extension on the left side bar in Alfred (Extension tab) and click on "Show in Finder". The source files for the extension will open up in Finder. 

4. Open the file "get\_klout\_score.py" and type in your Klout API key. Get your Klout API Key [here](http://developer.klout.com)

	![Type your Klout API Key](https://github.com/mashery/alfred-show-me-the-klout/raw/master/development/images/klout_api_key.png)
5. Open the file "twitter_auth.py" and type in your Twitter API key. Get your Twitter API Key [here](http://developer.twitter.com)

	![Type your Twitter API Key](https://github.com/mashery/alfred-show-me-the-klout/raw/master/development/images/twitter_api_key.png)
6. Install Tweepy. Open Terminal and type the following (If you run into permission issues, try with sudo) -

	<pre>easy_install tweepy</pre>
	
7. You're done. Just give Alfred a whirl now. Refer [How to Use](#how-to-use) above.


## Development

Be sure to follow the configuration steps above and use this step-by-step guide to tweak to your heart's content.

1. Grab the latest source
	<pre>git clone git://github.com/mashery/alfred-show-me-the-klout.git</pre>

2. Install Tweepy. Open Terminal and type the following (If you run into permission issues, try with sudo) -
	<pre>easy_install tweepy</pre>

4. All the Klout related action takes place in the file 'get\_klout\_score.py'

5. All the Twitter related action takes place in the file "get\_twitter\_details.py"

6. Tweak away!

## Problems?

* Make sure Tweepy module is installed. You can check that by running the following in a Python shell/prompt. Refer [Installation](#Installation) for details.

	<pre>
		python 
		help('modules')
	</pre>

## About 

* No warranty expressed or implied.  Software is as is.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly created by [Mashery Dev](http://dev.mashery.com)


