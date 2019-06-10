#! python3
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from lxml import etree
# Selecter = etree.HTML()

with open("index.html", "r") as file:
    fcontent = file.read()
    Selecter = etree.HTML(fcontent)
    sp = Selecter.xpath('//p234/@condition')
    print(sp)
    sp = Selecter.xpath('//ItemDefinitionGroup/@condition')
    print(sp)
