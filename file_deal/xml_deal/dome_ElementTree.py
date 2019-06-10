#! python3
# -*- coding:utf-8 -*-

from xml.etree.ElementTree import *


class Movies:
    def __init__(self,name=None,age=None,sex=None,score=None):
        self.name=name
        self.age=age
        self.sex=sex
        self.score=score

    def __str__(self):
        return "姓名：{0}，年龄：{1}，性别：{2}，成绩：{3}".format(self.name,self.age,self.sex,self.score)
people=[]
root=parse("students.xml")
student1=root.findall("student")
for p in student1:
    student=Student()
    student.name=p.find("name").text
    student.age = p.find("age").text
    student.sex = p.find("sex").text
    student.score = p.find("score").text
    people.append(student)
for p in people:
    print(p)
