# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DyttItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    brief = scrapy.Field()
    link = scrapy.Field()
    poster = scrapy.Field()
    download_url = scrapy.Field()

