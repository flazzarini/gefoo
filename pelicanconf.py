#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Frank Lazzarini'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'
SITENAME = u'General-Foo'
SITEDESCR = u'Linux, Technology and more'
SITEURL = 'http://localhost:8000'
THEME = 'theme/'
PATH = 'content'
STATIC_PATHS = ['images', 'uploads']
PLUGINS = ['pelican_youtube']

# Feed generation is usually not desired when developing
FEED_DOMAIN = 'http://www.gefoo.org'
FEED_RSS = ('feeds/feed.rss')

# Blogroll
LINKS = (('Two cents for your thoughts', 'http://yglodt.wordpress.com/'),
        ('Alldeeglechen Eifeler Regel FAIL', 'http://eifeler.wordpress.com/'),
        ('We understand technology', 'http://www.wuttech.com/'),
        ('Ceci n''est pas Luxembourg', 'http://www.cecinestpasluxembourg.eu/'),
        ('foobar.lu', 'http://www.foobar.lu'),
        ('Workaround', 'http://workaround.org/'),
        ('LussElsen', 'http://www.lusselsen.com'),
        ('KatrinElsen', 'http://www.katrinelsen.org'),)

# Social widget
SOCIAL = (('Linkedin', 'http://lu.linkedin.com/pub/frank-lazzarini/1a/a30/112'),
          ('Twitter', 'https://twitter.com/latztwn'),
          ('Lastfm', 'http://www.last.fm/user/latz'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
