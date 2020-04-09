# -*- coding: utf-8 -*-

# Scrapy settings for webspider project

BOT_NAME = 'webspider'

SPIDER_MODULES = ['webspider.spiders']
NEWSPIDER_MODULE = 'webspider.spiders'


USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'


ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
     'webspider.pipelines.MongoDBPipeline': 300, 
}

MONGO_URI = 'localhost:27017'
MONGO_DB = "noticias"
MONGO_COLLECTION = "artigos"
