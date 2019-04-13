# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList
from test01.items import Test01Item


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
            content = duanzi.xpath(".//div[@class='content']//text()").getall()
            content = ''.join(content).strip()
            # content = duanzi.xpath(".//span/text()").get().strip()
            # print('-'*40)
            # print(author)
            # print(content)
            # print('-'*40)
            # item = {"author": author, "content": content}
            item = Test01Item(author=author, content=content)
            yield item
        temp_url = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()[6:]
        next_url = 'https://www.qiushibaike.com/text/' + temp_url
        if not next_url:
            return
        else:
            yield scrapy.Request(next_url, callback=self.parse)
