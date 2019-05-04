#! python3
# -*- coding:utf-8 -*-
import scrapy
from juren.items import JurenItem


class JurenSpider(scrapy.Spider):
    """
    爬取第一层的内容
    """
    name = 'juren'
    allowed_domains = ['jurensucai.com']
    start_urls = ['http://www.jurensucai.com/juren2-1/']

    def parse(self, response):
        sucais = response.xpath("//div[@class='work-list-box']/div")
        base_url = 'http://www.jurensucai.com/'
        for sucai in sucais:
            return_url = sucai.xpath(".//div[@class='card-img']/a/@href").get()
            title = sucai.xpath(".//div[@class='card-img']/a/@title").get()
            src = sucai.xpath(".//div[@class='card-img']/a/img/@src").get()
            item = JurenItem(title=title, url=base_url+return_url, src=base_url+src)
            yield item
        temp_url = response.xpath("//div[@class='pg']//a[@class='nxt']/@href").get()
        if temp_url:
            next_url = 'http://www.jurensucai.com/' + temp_url
            yield scrapy.Request(next_url, callback=self.parse)
        else:
            return


# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
#
#
# class JurenSpider(CrawlSpider):
#     """
#     爬取第二层与第二层，但是第二层需要登录，登录问题未解决
#     """
#     name = 'juren'
#     allowed_domains = ['jurensucai.com']
#     start_urls = ['http://www.jurensucai.com/juren2-1/']
#
#     rules = (
#         # http://www.jurensucai.com/juren2-1/
#         Rule(LinkExtractor(allow=r'.+juren2-\d'), callback="parse_page", follow=True),
#         # http://www.jurensucai.com/wz-3393-1-1.html
#         Rule(LinkExtractor(allow=r'.+wz-\d+-1-1.html'), callback="parse_detail", follow=False)
#     )
#
#     def parse_page(self, response):
#         next_page = response.xpath("//div[@class='pg']//a[@class='nxt']/@href").get()
#         if next_page:
#             yield scrapy.Request('http://www.jurensucai.com/' + next_page, callback=self.parse_page)
#         else:
#             return
#
#     def parse_detail(self, response):
#         title = response.xpath("//h2[@id='thread_subject']/text()").get()
#         article_content = response.xpath("//td[@class='t_f']//text()").getall()
#         content = ''.join(article_content).strip()
#         download_url = response.xpath("//div[text()='免费下载链接']/../@href").get()
#         item = JurenItem(title=title, url=download_url)
#         yield item
