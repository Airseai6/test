# -*- coding:utf-8 -*-

crop = {
    "农业用地通用": "AGRL",
    "农业行种作物": "AGRR",
    "近距离种植作物": "AGRC",
    "果园": "ORCD",
    "干草": "HAY",
    "混交林": "FRST",
    "落叶林": "FRSD",
    "常绿林": "FRSE",
    "湿地混合": "WETL",
    "森林湿地": "WETF",
    "非森林湿地": "WETN",
    "牧场": "PAST",
    "夏季牧场": "SPAS",
    "冬季牧场": "WPAS",
    "禾本科牧草": "RNGE",
    "灌木": "RNGB",
    "美国西南部山脉": "SWRN",
    "水": "WATR",
    "玉米": "CORN",
    "玉米青贮": "CSIL",
    "甜玉米": "SCRN",
    "东部Gamagrass": "EGAM",
    "高粱": "GRSG",
    "高粱干草": "SGHY",
    "约翰逊草": "JHGR",
    "甘蔗": "SUGC",
    "春小麦": "SWHT",
    "冬小麦": "WWHT",
    "硬粒小麦": "DWHT",
    "黑麦": "RYE",
    "春大麦": "BARL",
    "燕麦": "OATS",
    "水稻": "RICE",
    "珍珠粟": "PMIL",
    "蒂莫西": "TIMO",
    "无芒雀麦": "BROS",
    "草甸雀麦草": "PECD",
    "高羊茅": "FESC",
    "肯塔基蓝草": "BLUG",
    "狗牙根": "BERM",
    "有冠麦草": "DCCY",
    "西麦草": "WWGR",
    "细麦草": "ZHCY",
    "意大利黑麦草": "RYEG",
    "俄罗斯野生蜀葵": "RYER",
    "阿尔泰野生蜀葵": "SFZB",
    "侧翼格拉马": "SIDE",
    "大须芒草": "BBLS",
    "小须芒草": "LBLS",
    "阿拉莫柳枝稷": "SWCH",
    "印度草": "INDN",
    "紫花苜蓿": "ALFA",
    "草木樨": "CLVS",
    "红三叶草": "CLVR",
    "Alsike三叶草": "CLVA",
    "黄豆": "SOYB",
    "豇豆": "CWPS",
    "绿豆": "MUNG",
    "利马豆": "LIMA",
    "扁豆": "LENT",
    "花生": "PNUT",
    "豌豆": "FPEA",
    "花园罐头豆": "PEAS",
    "田菁属": "SESB",
    "亚麻": "FLAX",
    "陆地棉花": "COTS",
    "陆地棉花2": "COTP",
    "烟草": "TOBC",
    "甜菜": "SGBT",
    "马铃薯": "POTA",
    "番薯": "SPOT",
    "胡萝卜": "CRRT",
    "洋葱": "ONIO",
    "向日葵": "SUNF",
    "春菜油": "CANP",
    "阿根廷春菜": "CANA",
    "芦笋": "ASPR",
    "西兰花": "BROC",
    "甘蓝": "CABG",
    "花椰菜": "CAUF",
    "芹菜": "CELR",
    "莴苣": "LETT",
    "菠菜": "SPIN",
    "青豆": "GRBN",
    "黄瓜": "CUCM",
    "茄子": "EGGP",
    "哈密瓜": "CANT",
    "蜜瓜": "HMEL",
    "西瓜": "WMEL",
    "甜椒": "PEPR",
    "草莓": "STRW",
    "番茄": "TOMA",
    "苹果": "APPL",
    "松树": "PINE",
    "橡木": "OAK",
    "白杨": "POPL",
    "蜂蜜豆科灌木": "MESQ",
    "葡萄园": "GRAP",
    "冬大麦": "WBAR",
    "油棕": "OILP",
    "橡胶树": "RUBR",
    "香蕉": "BANA",
    "画眉草": "TEFF",
    "咖啡": "COFF",
    "斑豆": "PTBN",
    "杏树": "ALMD",
    "Grarigue": "GRAR",
    "橄榄": "OLIV",
    "橙子": "ORAN",
    "化粪池区": "SEPT",
    "Maizhshl灌木": "LSGC",
    "Jinlumei灌木": "JLGC",
    "冰": "CNJX",
    "柳灌木": "MJGC",
    "贫瘠地区": "BALD",
    "Xiaohc混合": "HCCD",
    "浩泰混合": "HTCD",
    "荒漠": "HTHM",
    "云山": "QHZY",
    "阿尔泰野生蜀葵2": "HCZB",
    "阿尔泰野生蜀葵111": "HCZB",
}

# import pprint
# pp = pprint.PrettyPrinter(indent=4, depth=6)
# pp.pprint(crop)
# string = "#".join([k + ":" + v for k,v in crop.items()])

# import textwrap
# for line in textwrap.wrap(string, 50):
#     linedata = line.split("#")
#     # linedata = [s.rjust(18) for s in linedata]
#     # linedata = "".join(linedata)
#     # print((' {:>20}' * len(linedata)).format(*linedata))
#     print(linedata)


from prettytable import PrettyTable

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

def getPrettyTable(d, indent = 4):
    t = PrettyTable(["colunm" + str(i) for i in range(indent)] )
    s = [k + " " + v for k,v in d.items()]
    for i in list(chunkstring(s, indent)):
        if len(i) < indent:
            i += [""] * (indent - len(i))
        try:
            t.add_row(i)
            # print(type(t))
        except Exception as e:
            import traceback
            traceback.print_exc()
    return t

print(getPrettyTable(crop, 4))
# getPrettyTable(crop, 4)

