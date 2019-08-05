# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
 Author: zhiwei.xu
 Date: 2019-08-04 18:05:12
 LastEditors: zhiwei.xu
 LastEditTime: 2019-08-05 17:12:51
'''

from __future__ import unicode_literals

AUTHOR = 'Chihwei-Hsu'
SITENAME = "Hsu's Home"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh_cn'

THEME = "elegant"
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

PORT = 9999

BIND = '0.0.0.0'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
# IPYNB_USE_METACELL = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
