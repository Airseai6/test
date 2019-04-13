# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wxapp.items import WxappItem


class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        # Rule(LinkExtractor(allow=r'http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=\d'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r'.+article-.+\.html'), callback="parse_detail", follow=False)
    )

    def parse_detail(self, response):
        title = response.xpath("//h1[@class='ph']/text()").get()
        author = response.xpath("//p[@class='authors']/a/text()").get()
        pub_time = response.xpath("//p[@class='authors']/span/text()").get()
        article_content = response.xpath("//td[@id='article_content']//text()").getall()
        content = ''.join(article_content).strip()
        # print('-'*40)
        # print(title)
        # print(article_content)
        item = WxappItem(title=title, author=author, pub_time=pub_time, content=content)
        yield item

