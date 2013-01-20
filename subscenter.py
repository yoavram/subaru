# -*- coding: utf-8 -*-
import sys
import feedparser
import spynner
import requests
from StringIO import StringIO
import pyquery
from zipfile import ZipFile

SITE_URL = 'http://www.subscenter.org'
OUTPUT_PATH = r'd:\videos'
LATEST_FEED_URL = SITE_URL + "/he/feeds/all/latest/"
FAVORITES = (u'משפחה מודרנית', u'האנטומיה של גריי')
HELP_OPTIONS = ('-h', '?','--help', '/?', '/h', '/help', '-help', '--h')

def parse_subtitles_links(url):
        br=spynner.Browser()
        br.load(url)
        p = pyquery.PyQuery(br.html)
        h=p('.pageName:first')[0]
        title = h.text_content()
        links = []
        for btn in p(".minibutton"):
                onclick = btn.attrib['onclick']
                start = onclick.index("('") + 2
                stop = onclick[start:].index("')") + start
                lnk = onclick[start:stop]
                links.append(lnk)
        if links:
                print "Found subtitles for", title
        else:
                print "Did not find subtitles for", title
        return links

def download_links(links):
        for lnk in links:
                r = requests.get(SITE_URL + lnk)
                if r.ok:
                        z = ZipFile(StringIO(r.content))
                        z.extractall(OUTPUT_PATH)
                        z.close()
                else:
                        print 'Failed getting link:', lnk
        return len(links)

def latest_episodes(feed_url):
        feed = feedparser.parse( feed_url )
        episodes = {}
        for epi in feed['items']:
                stop = epi['link'].index('?')
                link = epi['link'][:stop]
                episodes[epi['title']] = link
        return episodes

def parse_latest_favorites():
        episodes = latest_episodes(LATEST_FEED_URL)
        links = []
        for title, url in episodes.items():
                for fav in FAVORITES:
                        if title.startswith(fav):
                                print "Found subtitles for", unicode(title)
                                links.extend(parse_subtitles_links(url))
        return links

def create_episode_url(title, season, episode):
        # 'http://www.subscenter.org/he/subtitle/series/blue-bloods/3/9/'
        return '%s/he/subtitle/series/%s/%d/%d/' % (SITE_URL, title, season, episode)

def create_movie_url(title):
        # 'http://www.subscenter.org/he/subtitle/movie/the-five-year-engagement/'
        return '%s/he/subtitle/movie/%s' % (SITE_URL, title)

if __name__=='__main__':
        if len(sys.argv) == 2 and sys.argv[1] in HELP_OPTIONS:
                print '''Usage:\n
Download latest from favorites:\n
                %s\n
Download movie subtitle:
                %s <movie-title> [subtitle-keyword]\n
Download TV episode:
                %s <show-title> <season-number> <episode-number> [subtitle-keyword]\n
Print this help message:
                %s -h\n''' % (sys.argv[0], sys.argv[0], sys.argv[0], sys.argv[0])
                exit()
        elif len(sys.argv) >= 4:
                # tv episode
                title, season, episode = sys.argv[1], sys.argv[2], sys.argv[3]
                episode_url = create_episode_url(title, int(season), int(episode))
                links = parse_subtitles_links(episode_url)
                if len(sys.argv) > 4:
                        keyword = sys.argv[4]
        elif len(sys.argv) >= 1:
                # movie
                title  = sys.argv[1]
                movie_url = create_movie_url(title)
                links = parse_subtitles_links(movie_url) # TODO test
                if len(sys.argv) > 1:
                        keyword = sys.argv[2]
        else:
                links = parse_latest_favorites()
        if keyword:
                links = filter(lambda x: keyword in x, links)
        if links:
                download_links(links) # TODO test for movies
