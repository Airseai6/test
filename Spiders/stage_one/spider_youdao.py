#! python
# -*- coding:utf-8 -*-
"""
爬虫
1、确定要爬去的目标
2、分析目标网站的数据
3、编写代码--检测--解决bug--代码优化
4、展示效果

import request json
Http --无状态-无连接 --快速
Https --CA证书 --SSL协议加密
爬虫 --就是一个伪造的客户端 --隐藏自己爬虫程序身份
常见反爬手段和应对方法:
1.设置header反爬虫
	在代码中设置User-Agent
2.IP访问频率，超过某个阀值
	2.1：设置延迟time
	2.2：使用IP代理 准备IP代理池
3.动态页面的反爬虫
	借助ajax框架 --js生成---selenium

1.Get   --向服务器获取数据
2.Post  --向服务器提交数据
"""
import request
content = input('Please input: ')
request_url = request.Request('http://fanyi.youdao.com/?keyfrom=fanyi.logo')

Form_Data={
	'':'',
	'':'',
	'':'',
	'':'',
	'':'',
	'':'',
	'':'',
}


