#! python3
# -*- coding:utf-8 -*-

import xml.etree.ElementTree as ET


class Movies:
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    def __str__(self):
        return "CurrentData：{0}，type：{1}，format：{2}，year：{3}，rating：{4}，stars：{5}，" \
               "description：{6}".format(self.CurrentData,self.type,self.format,self.year,
                                        self.rating,self.stars,self.description)


movies = []
root = ET.parse("movies.xml")
print(root)
# items = root.findall("movie")
items = root.getroot()
print(items)
for p in items:
    print('title: ', p.attrib)
    movie = Movies()
    movie.type = p.find("type").text
    print(movie.type)
    movie.format = p.find("format").text
    # movie.year = p.find("year").text
    movie.rating = p.find("rating").text
    movie.stars = p.find("stars").text
    movie.description = p.find("description").text
    movies.append(movie)
for p in items:
    print(p)
