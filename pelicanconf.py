#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mridul Malpotra'
SITENAME = u'NILMTK Blog - Mridul Malpotra'
SITEURL = ''

PATH = 'content'
THEME = "/home/mridul/nilmtk/pelican/pelican-themes/fresh"

TIMEZONE = 'Asia/Kolkata'
DISPLAY_PAGES_ON_MENU = True
DEFAULT_LANG = u'en'

#THEME = '/home/mridul/nilmtk/pelican/pelican-themes/voidy-bootstrap/'
STYLESHEETS = ("pygment.css", "voidybootstrap.css",)
CUSTOM_ARTICLE_SHARING = "sharing.html"
CUSTOM_ARTICLE_SCRIPTS = "sharing_scripts.html"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('NILMTK','https://github.com/nilmtk/nilmtk'),
		('Pelican', 'http://getpelican.com/'),
		('Python', 'http://python.org/'),
		)

# Social widget
SOCIAL = (('My Github', 'https://github.com/mridulmalpotra'),
	('Google+', 'https://plus.google.com/+MridulMalpotra'),
	('Facebook', 'https://www.facebook.com/mridul.malpotra')
	)

DEFAULT_PAGINATION = 10

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
