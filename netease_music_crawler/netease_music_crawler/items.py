# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NeteaseMusicCrawlerItem(scrapy.Item):
    song =scrapy.Field()
    album = scrapy.Field()
    artist = scrapy.Field()
