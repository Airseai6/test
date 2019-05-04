# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import requests


class JurenPipeline(object):
    def __init__(self):
        self.fp = open('Jurensucai.json', 'w', encoding='utf-8')
        self.fold_name = r'E:\02_Scripts\Python\test\Spiders\scrapy_demo\juren\Pictures'
        if not os.path.exists(self.fold_name):
            os.mkdir(self.fold_name)

    def open_spider(self, spider):
        print('beginning~~~~')

    def process_item(self, item, spider):
        item_json = json.dumps(dict(item), ensure_ascii=False)
        self.fp.write(item_json + '\n')
        with open('{}//{}.jpg'.format(self.fold_name, item['title']), 'wb') as f:
            req = requests.get(item['src'])
            f.write(req.content)
        return item

    def close_spider(self, spider):
        self.fp.close()
        print('finished')

