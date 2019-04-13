#! python3
# -*- coding:utf-8 -*-

if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute('scrapy crawl wxapp_spider'.split())
