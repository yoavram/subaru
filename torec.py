# -*- coding: cp1255 -*-
# http://wiki.python.org/moin/RssLibraries
# http://code.google.com/p/feedparser/
import feedparser
from urllib import urlopen, urlretrieve

subtitle_extension = ".srt"

print "AutoSub starting"

with open('torec.url') as f:
	feed_url = f.read().strip()
feed = feedparser.parse( feed_url )
sub_urls = {}

for item in feed[ "items" ]:
    for k,v in item.items():
            print k, "\t\t", v
            print
    urlretrieve(item[ "link" ], "tmp.html")
    break
print "AutoSub finished"

