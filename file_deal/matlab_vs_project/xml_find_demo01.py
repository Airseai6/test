#! python3
# -*- coding:utf-8 -*-

from lxml import etree

# with open("Three_Phase_Inverter_V2017a.vcxproj", "r") as file:
# with open("test.txt", "r", encoding='utf-8') as file:
#     fcontent = file.read()
#     print(fcontent)
#     Selecter = etree.HTML(fcontent)
#     print(Selecter)
#     # result = etree.tostring(Selecter).decode('utf-8')
#     sp = Selecter.xpath('//ItemDefinitionGroup/@Condition')
#
#     print(sp)


import xml.dom.minidom
dom = xml.dom.minidom.parse(r'test.txt')
root = dom.documentElement
print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
print(root.ELEMENT_NODE)
