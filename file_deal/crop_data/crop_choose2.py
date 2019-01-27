#! python
# -*- coding:utf-8 -*-
import sys
import time
crop ={
    "1": "AGRL",
    "2": "AGRR",
    "3": "AGRC",
    "4": "ORCD",
    "5": "HAY",
    "6": "FRST",
    "7": "FRSD",
    "8": "FRSE",
    "9": "WETL",
    "10": "WETF",
    "11": "WETN",
    "12": "PAST",
    "13": "SPAS",
    "14": "WPAS",
    "15": "RNGE",
    "16": "RNGB",
    "17": "SWRN",
    "18": "WATR",
    "19": "CORN",
    "20": "CSIL",
    "21": "SCRN",
    "22": "EGAM",
    "23": "GRSG",
    "24": "SGHY",
    "25": "JHGR",
    "26": "SUGC",
    "27": "SWHT",
    "28": "WWHT",
    "29": "DWHT",
    "30": "RYE",
    "31": "BARL",
    "32": "OATS",
    "33": "RICE",
    "34": "PMIL",
    "35": "TIMO",
    "36": "BROS",
    "37": "BROM",
    "38": "FESC",
    "39": "BLUG",
    "40": "BERM",
    "41": "CWGR",
    "42": "WWGR",
    "43": "SWGR",
    "44": "RYEG",
    "45": "RYER",
    "46": "RYEA",
    "47": "SIDE",
    "48": "BBLS",
    "49": "LBLS",
    "50": "SWCH",
    "51": "INDN",
    "52": "ALFA",
    "53": "CLVS",
    "54": "CLVR",
    "55": "CLVA",
    "56": "SOYB",
    "57": "CWPS",
    "58": "MUNG",
    "59": "LIMA",
    "60": "LENT",
    "61": "PNUT",
    "62": "FPEA",
    "63": "PEAS",
    "64": "SESB",
    "65": "FLAX",
    "66": "COTS",
    "67": "COTP",
    "68": "TOBC",
    "69": "SGBT",
    "70": "POTA",
    "71": "SPOT",
    "72": "CRRT",
    "73": "ONIO",
    "74": "SUNF",
    "75": "CANP",
    "76": "CANA",
    "77": "ASPR",
    "78": "BROC",
    "79": "CABG",
    "80": "CAUF",
    "81": "CELR",
    "82": "LETT",
    "83": "SPIN",
    "84": "GRBN",
    "85": "CUCM",
    "86": "EGGP",
    "87": "CANT",
    "88": "HMEL",
    "89": "WMEL",
    "90": "PEPR",
    "91": "STRW",
    "92": "TOMA",
    "93": "APPL",
    "94": "PINE",
    "95": "OAK",
    "96": "POPL",
    "97": "MESQ",
    "98": "GRAP",
    "99": "WBAR",
    "100": "OILP",
    "101": "RUBR",
    "102": "BANA",
    "103": "TEFF",
    "104": "COFF",
    "105": "PTBN",
    "106": "ALMD",
    "107": "GRAR",
    "108": "OLIV",
    "109": "ORAN",
    "110": "SEPT",
    "122": "LSGC",
    "123": "JLGC",
    "124": "CNJX",
    "125": "MJGC",
    "126": "PECD",
    "111": "BALD",
    "112": "HCCD",
    "113": "XSCY",
    "114": "ZHCY",
    "115": "SFZB",
    "117": "HTCD",
    "118": "HTHM",
    "119": "QHZY",
    "120": "HCZB",
    "121": "DCCY"
}


def crop_data():
    file = "crop_0.dat"
    # 把内容写到内存
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for key in crop:
        # 查找替换内容
        index = 0
        for line in lines:
            if crop[key] in line:
                temp_index = index
            index += 1
        database = lines[temp_index: temp_index+5]
        # 写文件
        new_file = file.replace('0', key)
        with open(new_file, "w", encoding="utf-8") as f_w:
            lines[581:585] = database[1:]
            for line in lines:
                f_w.write(line)
        print(new_file + ' 生成完毕，，，')


if __name__ == '__main__':
    crop_data()