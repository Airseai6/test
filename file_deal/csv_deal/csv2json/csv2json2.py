# 下面的工具可以方便的将CSV格式文件转换成json文件格式

import sys, json


def csv2json(input_file):
	# 获取输入数据
	# input_file = sys.argv[1]
	# input_file = 'DB4.csv'
	lines = open(input_file, "r", encoding="utf_8_sig").readlines()
	lines = [line.split(',') for line in lines]
	parsed_datas = []
	keys = []
	values = []
	for line in lines:
		keys.append(line[0])
		values.append(line[1].strip())

	parsed_datas.append(dict(zip(keys, values)))

	json_str = json.dumps(parsed_datas, ensure_ascii=False, indent=4)
	output_file = input_file.replace("csv", "json")

	# write to the file
	f = open(output_file, "w", encoding="utf-8")
	f.write(json_str)
	f.close()


if __name__ == '__main__':
	input_file = '太阳时.csv'
	csv2json(input_file)
	print("解析结束！")
