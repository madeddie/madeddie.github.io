#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Edwin Hermans'
SITENAME = u'madeddieclopaedia'
SITEURL = 'http://madeddie.github.io'
TIMEZONE = 'Europe/Amsterdam'
THEME = 'themes/bootstrap'
DIRECT_TEMPLATES = (('index', 'blog', 'tags', 'categories', 'archives'))
PAGINATED_DIRECT_TEMPLATES = (('blog', ))

DEFAULT_LANG = u'en'

STATIC_PATHS = ['images', 'README.md']
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('inside Habbie\'s mind', 'http://7bits.nl/blog/'),
          ('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/madeddie'),
          ('github', 'http://github.com/madeddie'),)

GITHUB_URL = 'http://github.com/madeddie'
TWITTER_USERNAME = 'madeddie'

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
