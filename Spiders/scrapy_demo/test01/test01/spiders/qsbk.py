# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList


class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        # print('='*30)
        # print(response.xpath("//div[@id='content-left']"))
        # print('='*30)
        duanzidivs = response.xpath("//div[@id='content-left']/div")
        for duanzi in duanzidivs:
            author = duanzi.xpath(".//h2/text()").get().strip()
            # content = duanzi.xpath(".//div[@class='content']//text()").getall()
            # content = ''.join(content)
            content = duanzi.xpath(".//span/text()").get().strip()
            # content = duanzi.xpath(".//span")
            print('-'*40)
            print(author)
            print(content)
            print('-'*40)
