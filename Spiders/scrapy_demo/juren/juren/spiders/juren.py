#! python3
# -*- coding:utf-8 -*-
import scrapy
from juren.items import JurenItem


class JurenSpider(scrapy.Spider):
    name = 'juren'
    allowed_domains = ['jurensucai.com']
    start_urls = ['http://www.jurensucai.com/juren2-1/']

    def parse(self, response):
        sucais = response.xpath("//div[@class='work-list-box']/div")
        for sucai in sucais:
            return_url = sucai.xpath(".//div[@class='card-img']/a/@href").get()
            title = sucai.xpath(".//div[@class='card-img']/a/@title").get()
            item = JurenItem(title=title, url='http://www.jurensucai.com/' + return_url)
            yield item
        temp_url = response.xpath("//div[@class='pg']//a[@class='nxt']/@href").get()
        if temp_url:
            next_url = 'http://www.jurensucai.com/' + temp_url
            yield scrapy.Request(next_url, callback=self.parse)
        else:
            return
