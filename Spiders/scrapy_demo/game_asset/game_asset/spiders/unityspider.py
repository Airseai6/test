# -*- coding: utf-8 -*-
import scrapy
from game_asset.items import GameAssetItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class UnityspiderSpider(CrawlSpider):
    name = 'unityspider'
    allowed_domains = ['game-asset.net/unity.net']
    start_urls = ['https://game-asset.net/unity/page/1/']
    rules = (
        Rule(LinkExtractor(allow=r'https://game-asset.net/unity/page/\d/'), callback="parse_page", follow=True),
        # https: // game-asset.net / unity / 2d-asset / 3318-fantasy-game-button-maker.html
        # https: // game-asset.net / unity / 3d-models / 2627-little-dragons-tiger.html
        # https://game-asset.net/unity/animation/3185-cover-rifle-animset-pro.html
        # https://game-asset.net/unity/audio/3088-rts-and-moba-voice-pack.html
        # https: // game-asset.net / unity / shaders / 3298-holo-fx-pack.html
        # https: // game-asset.net / unity / particle-systems / 3299-imagy-vfx.html
        # https: // game-asset.net / unity / tools / 2505-ultimate-mobile-pro.html
        Rule(LinkExtractor(allow=r'.+/unity/.{2,20}/.*'), callback='parse_item', follow=True),
    )

    def parse_page(self, response):
        # details = response.xpath('//div[@id="dle-content"]/div[@class="story-short col-xs-6 col-sm-4 col-md-4"]/div').get()
        detail = response.xpath('//div[@class="img_crop"]/a/@href').get()
        yield scrapy.Request(detail, callback=self.parse_page)

        next_page = response.xpath('//em[@class="next"]/a/@href').get()
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse_page)
        else:
            return

    def parse_item(self, response):
        title = response.xpath("//h1/text()").get()
        asset_type = response.xpath('//li[@class="lcat"]/a/text()').getall()
        asset_type = ' '.join(asset_type).strip()
        content = response.xpath('//div[@class="full-str clearfix"]//span/text()').getall()
        content = ''.join(content).strip()
        picture = response.xpath('//div[@style="text-align:center;"]/img/@src').get()
        picture = 'https://game-asset.net/' + picture
        hitfile_download_url = response.xpath("//a[text()='Hitfile']/@href").get()
        nitroflare_download_url = response.xpath("//a[text()='Nitroflare']/@href").get()
        item = GameAssetItem(title=title, Type=asset_type, content=content, picture=picture,
                             hitfile_download_url=hitfile_download_url, nitroflare_download_url=nitroflare_download_url)
        yield item
