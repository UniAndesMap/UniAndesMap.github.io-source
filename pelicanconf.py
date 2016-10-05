#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

AUTHOR = u'BogoMap Team, Proyecto Curuba'
SITENAME = u'DuitaMap - Rutas de buses de Duitama'
SITESUBTITLE = 'Transporte Urbano Duitama, Boyacá, Colombia'
SITEDESCRIPTION = 'Mapa de rutas de buses de Duitama'
SITEKEYWORDS = 'Bus, Buses, Rutas, Ruta, Transporte, Colombia, Duitama, OpenStreetMap, Transporte público, Datos Abiertos, Open Data'

USE_LESS = True
SITEURL = 'https://jhergon.github.io'
#SITEURL = 'http://localhost:8000'
#SITELOGO = '/images/mapanica-rutas.png'
THEME = 'themes/mombacho'

FAVICON = '/images/favicon.ico'
ROBOTS = 'index, follow'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = False
TAG_SAVE_AS = False
ARCHIVES_SAVE_AS = False
DIRECT_TEMPLATES = ('index', 'embed')

CC_LICENSE = { 'name': 'Creative Commons Attribution-ShareAlike', 'version':'4.0', 'slug': 'by-sa' }

PATH = 'content'
STATIC_PATHS = ['images','php']

TIMEZONE = 'America/Bogota'

DEFAULT_LANG = u'es'
OG_LOCALE = u'es_CO'
DEFAULT_DATE_FORMAT = ('%d %B %Y')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('email', 'mailto:contacto@bogomap.co'),
          ('facebook', 'http://www.facebook.com/BogoMap'),
          ('twitter', 'http://www.twitter.com/bogomap'),
          )

MENUITEMS = (('Rutas Duitamap', '/index.html', 'public-transport'),
             ('BogoMap', 'http://BogoMap.co', 'community'),
          )

DEFAULT_PAGINATION = False
