# -*- coding: utf-8 -*-
import scrapy


class Music163Spider(scrapy.Spider):
    name = 'music163'
    allowed_domains = ['music.163.com']
    start_urls = ['https://music.163.com/#/discover/toplist']

    def parse(self, response):
        music_top_list = response.xpath("//tbody")
        # print(music_top_list)
        for music in music_top_list:
            # music_name = music.xpath(".//tr/td/div/div/div/span/a/b/text()").get()
            music_name = music.xpath("//span[@class='txt']//b/@title").extract()
            print(music_name)
