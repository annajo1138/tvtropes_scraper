# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TvtropesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    all_links = scrapy.Field()
    url_name = scrapy.Field()
    namespace = scrapy.Field()
    can_review = scrapy.Field()
