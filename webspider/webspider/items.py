# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebspiderItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    article = scrapy.Field()
    excerpt = scrapy.Field()
    date = scrapy.Field()
    etag = scrapy.Field()
