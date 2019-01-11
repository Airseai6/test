#! python
# -*- coding:utf-8 -*-
import sys
import time
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
    "阿尔泰野生蜀葵2": "HCZB"
}


def hello():
    print('-------------------------------------------')
    print('   请确保“crop_0.dat”文件与脚本在同一目录下。   ')
    print('-------------------------------------------')
    # print("""
    #     农业用地通用      农业行种作物   近距离种植作物  果园    干草   混交林    落叶林 
    #     常绿林  湿地混合   森林湿地    非森林湿地   牧场  夏季牧场    冬季牧场    禾本科牧草   
    #     灌木  美国西南部山脉 水   玉米 玉米青贮  甜玉米    东部Gamagrass 
    #     高粱   高粱干草  约翰逊草  甘蔗 春小麦 冬小麦 硬粒小麦    黑麦  春大麦 
    #     燕麦   水稻 珍珠粟 蒂莫西 无芒雀麦    草甸雀麦草   高羊茅 肯塔基蓝草   
    #     狗牙根  有冠麦草   西麦草 细麦草 意大利黑麦草  俄罗斯野生蜀葵 
    #     阿尔泰野生蜀葵   侧翼格拉马  大须芒草     小须芒草  阿拉莫柳枝稷  印度草 
    #     紫花苜蓿     草木樨    红三叶草    Alsike三叶草    黄豆  豇豆  绿豆  利马豆    扁豆  
    #     花生  豌豆  花园罐头豆   田菁属 亚麻   陆地棉花   陆地棉花2     烟草    
    #     甜菜   马铃薯    番薯    胡萝卜   洋葱  向日葵 春菜油 阿根廷春菜  芦笋   西兰花 
    #     甘蓝   花椰菜    芹菜 莴苣  菠菜   青豆  黄瓜  茄子  哈密瓜 蜜瓜  西瓜  甜椒  草莓  
    #     番茄  苹果  松树  橡木  白杨  蜂蜜豆科灌木  葡萄园 冬大麦 油棕  橡胶树 香蕉  
    #     画眉草 咖啡    斑豆    杏树  Grarigue    橄榄  橙子   化粪池区    Maizhshl灌木
    #     Jinlumei灌木 冰    柳灌木 草甸雀麦草   贫瘠地区     Xiaohc混合    有冠麦草   
    #     细麦草 阿尔泰野生蜀葵  浩泰混合  荒漠  云山    阿尔泰野生蜀葵2   有冠麦草
    #     """)
    print("""
            农业用地通用、 农业行种作物、 近距离种植作物、 果园、干草、 混交林、落叶林、
            常绿林、 湿地混合、森林湿地、非森林湿地、 牧场、夏季牧场、冬季牧场、禾本科牧草、
            灌木、 美国西南部山脉、 水、 玉米、 玉米青贮、 甜玉米、 东部Gamagrass、
            高粱、 高粱干草、 约翰逊草、 甘蔗、春小麦、冬小麦、硬粒小麦、黑麦、春大麦、
            燕麦、 水稻、 珍珠粟、 蒂莫西、 无芒雀麦、 草甸雀麦草、 高羊茅、 肯塔基蓝草、
            狗牙根、 有冠麦草、西麦草、细麦草、意大利黑麦草、俄罗斯野生蜀葵、
            阿尔泰野生蜀葵、  侧翼格拉马、 大须芒草、 小须芒草 、阿拉莫柳枝稷、印度草、
            紫花苜蓿、 草木樨、红三叶草、Alsike三叶草、 黄豆、 豇豆、 绿豆、 利马豆、扁豆、
            花生、 豌豆、 花园罐头豆、 田菁属、 亚麻、 陆地棉花、 陆地棉花2、  烟草、
            甜菜、 马铃薯、 番薯、 胡萝卜、洋葱、 向日葵、春菜油、阿根廷春菜、 芦笋、西兰花、
            甘蓝、 花椰菜、芹菜、 莴苣、 菠菜、青豆、黄瓜、茄子、哈密瓜、蜜瓜、西瓜、甜椒、草莓、
            番茄、苹果、松树、橡木、白杨、蜂蜜豆科灌木、葡萄园、冬大麦、油棕、橡胶树、香蕉、
            画眉草、咖啡、  斑豆、杏树、 Grarigue、橄榄 、橙子、 化粪池区、 Maizhshl灌木、
            Jinlumei灌木、 冰、柳灌木、草甸雀麦草、贫瘠地区、 Xiaohc混合、 有冠麦草、
            细麦草、阿尔泰野生蜀葵、 浩泰混合、 荒漠、 云山、 阿尔泰野生蜀葵2、 有冠麦草
            """)
    print('-------------------------------------------')
    global name
    name = input('请输入上面一种作物地形 >>>:')
    if name in crop:
        return crop[name]
    else:
        print('输入有误，程序即将退出。')
        time.sleep(3)
        sys.exit()


def crop_data():
    file = "crop_0.dat"
    item = hello()
    # 把内容写到内存
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    # 查找替换内容
    index = 0
    for line in lines:
        if item in line:
            temp_index = index
        index += 1
    database = lines[temp_index: temp_index+5]
    print('-------------------------------------------')
    print('正在将 ' + str(database[0].split('\n')) + ' 处参数：')
    print(database[1].split('\n'))
    print(database[2].split('\n'))
    print(database[3].split('\n'))
    print(database[4].split('\n'))
    print('替换至  129  HCCD  6  处（此标题未改动）。')
    print('-------------------------------------------')
    # 写文件
    new_file = file.replace('0', name)
    with open(new_file, "w", encoding="utf-8") as f_w:
        lines[581:585] = database[1:]
        for line in lines:
            f_w.write(line)
    print(new_file + ' 生成完毕，程序即将退出...')
    time.sleep(3)
    sys.exit()


if __name__ == '__main__':
    crop_data()