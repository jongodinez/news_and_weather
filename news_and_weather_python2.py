import pyttsx
import time

#****use this to get voices listing****#

# voices = engine.getProperty('voices')
# for voice in voices:
#    #engine.setProperty('voice', voice.id)  # changes the voice
#    #engine.say('The quick brown fox jumped over the lazy dog.')
#    print voice.id

#****use this to get voices listing****#

tts = pyttsx.init()
tts.setProperty('voice', 'en-scottish')
#engine.setProperty('voice', 'english+f3')
tts.setProperty('rate', 190)

import feedparser

#get weather
weather_feed=feedparser.parse('http://www.rssweather.com/zipcode/95687/rss.php')
weather_entry = weather_feed.entries[0].title
weather_descr = weather_feed.entries[2].description
print(weather_entry)
tts.say(weather_entry)
tts.say('Tomorrows forecast')
print('Tomorrow\'s forecast: \n' + weather_descr + "\n")
tts.say(weather_descr)
#tts.runAndWait()


#get news
tts.say('World news headlines')
news_feed = feedparser.parse('http://www.npr.org/rss/rss.php?id=1001')
for entry in news_feed.entries:
	news_entry = entry.title
	print news_entry
for n in range (0,3):
	news_entry = news_feed.entries[n].title
	tts.say("item " + str(n+1))
	tts.say(news_entry, 'news_entry')
