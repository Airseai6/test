# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GameAssetItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    Type = scrapy.Field()
    content = scrapy.Field()
    picture = scrapy.Field()
    hitfile_download_url = scrapy.Field()
    nitroflare_download_url = scrapy.Field()
