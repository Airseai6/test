#! python3
# -*- coding:utf-8 -*-
import scrapy
from juren.items import JurenItem


# class JurenSpider(scrapy.Spider):
#     """
#     爬取第一层的内容
#     """
#     name = 'juren'
#     allowed_domains = ['jurensucai.com']
#     start_urls = ['http://www.jurensucai.com/juren2-1/']
#
#     def parse(self, response):
#         sucais = response.xpath("//div[@class='work-list-box']/div")
#         # print(sucais)
#         # print(type(sucais))
#
#         base_url = 'http://www.jurensucai.com/'
#         for sucai in sucais:
#             return_url = sucai.xpath(".//div[@class='card-img']/a/@href").get()
#             title = sucai.xpath(".//div[@class='card-img']/a/@title").get()
#             # print(title)
#             src = sucai.xpath(".//div[@class='card-img']/a/img/@src").get()
#             item = JurenItem(title=title, url=base_url+return_url, src=base_url+src)
#             yield item
#         temp_url = response.xpath("//div[@class='pg']//a[@class='nxt']/@href").get()
#         if temp_url:
#             next_url = 'http://www.jurensucai.com/' + temp_url
#             yield scrapy.Request(next_url, callback=self.parse)
#         else:
#             return


from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from scrapy import FormRequest


class JurenSpider(CrawlSpider):
    """
    爬取第二层与第二层，但是第二层需要登录，登录问题未解决
    """
    name = 'juren'
    allowed_domains = ['jurensucai.com']
    start_urls = ['http://www.jurensucai.com/juren2-1/']
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'ydjn_2132_sid=j9smFx; ydjn_2132_saltkey=GfFnK7kN; ydjn_2132_lastvisit=1557558524; ydjn_2132_st_p=0%7C1557562152%7C5804c841d402defc176b7db7e66db4af; ydjn_2132_sendmail=1; ydjn_2132_seccode=79.d19900f4956ca5941f; ydjn_2132_lastact=1557562978%09member.php%09register; ydjn_2132_ulastactivity=8e27cNLWZykrISkJBlXGJfXa7DKa8fNARtx0ziAU87QRSmKsqHES; ydjn_2132_auth=8208ynZAL9PNdh70ss0j0PZGXN4%2BjACRc1AhiKFNYt9acbbJn9sH%2BFfvDjPPHYw%2B8IdtH6iherGPju4W%2FEQ5t0g; ydjn_2132_creditnotice=0D0D2D0D0D0D0D0D0D149; ydjn_2132_creditbase=0D0D0D0D0D0D0D0D0; ydjn_2132_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95',
        'Host': 'www.jurensucai.com',
        'Referer': 'http://www.jurensucai.com/member.php?mod=register',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
    rules = (
        # http://www.jurensucai.com/juren2-1/
        Rule(LinkExtractor(allow=r'.+juren2-\d'), callback="parse_page", follow=True),
        # http://www.jurensucai.com/wz-3393-1-1.html
        Rule(LinkExtractor(allow=r'.+wz-\d+-1-1.html'), callback="parse_detail", follow=False)
    )

    def start_requests(self):
        return [Request('http://www.jurensucai.com/juren2-1/', meta={'cookiejar':1}, callback=self.post_login, method="POST")]

    def post_login(self, response):
        # html=BeautifulSoup(response.text,"html.parser")
        # for input in html.find_all('input'):
        #     if 'name' in input.attrs and input.attrs['name'] == 'lt':
        #         lt=input.attrs['value']
        #     if 'name' in input.attrs and input.attrs['name'] == 'execution':
        #         e1=input.attrs['value']
        # data={'username':'18210504923','password':'jrsc123','lt':lt,'execution':e1,'_eventId':'submit'}
        data={'username':'18210504923','password':'jrsc123','_eventId':'submit'}
        return [FormRequest.from_response(response,
                                          meta={'cookiejar':response.meta['cookiejar']},
                                          headers=self.headers,
                                          formdata=data,
                                          callback=self.after_login,)]

    def after_login(self,response):
        header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',}
        return [Request("http://www.jurensucai.com/juren2-1/",meta={'cookiejar':response.meta['cookiejar']},headers=header,callback=self.parse_page)]

    def parse_page(self, response):
        next_page = response.xpath("//div[@class='pg']//a[@class='nxt']/@href").get()
        if next_page:
            yield scrapy.Request('http://www.jurensucai.com/' + next_page, callback=self.parse_page)
        else:
            return

    def parse_detail(self, response):
        title = response.xpath("//h2[@id='thread_subject']/text()").get()
        article_content = response.xpath("//td[@class='t_f']//text()").getall()
        content = ''.join(article_content).strip()
        download_url = response.xpath("//div[text()='免费下载链接']/../@href").get()
        item = JurenItem(title=title, url=download_url)
        yield item
