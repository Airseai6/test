import requests
import json
# 面向对象设计模式 --> 面向对象

class Spider(object):
    def start_request(self):
        # 1. 获取接口整体数据 requests
        for i in range(0, 1001, 20):
            url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=" + str(i) + "&limit=20"
            print("正在抓取网址：" + url)
            response = requests.get(url)
            py_data = json.loads(response.content.decode())
            if py_data == []:
                return "==========抓取完毕！=========="
            # 2. 抽取想要的数据
            for i in py_data:
                items = {"影片名称": i['title'], "影片地区": i['regions'][0], "上映时间":i['release_date'], "影片评分": i['score']}
                print(items)
                content = json.dumps(items, ensure_ascii=False) + ",\n"
                # 3. 保存数据
                with open("douban.json", "a", encoding="utf-8") as f:
                    f.write(content)


spider = Spider()
print(spider.start_request())