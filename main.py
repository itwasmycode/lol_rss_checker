import feedparser
import requests


URL = requests.get("https://tr.leagueoflegends.com/tr/rss.xml")



URL_FEED = feedparser.parse(URL.content)

for entry in URL_FEED.entries:
    print(entry.title)
