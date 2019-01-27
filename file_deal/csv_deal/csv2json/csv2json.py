# 下面的工具可以方便的将CSV格式文件转换成json文件格式

import sys, json

# 获取输入数据
# input_file = sys.argv[1]
input_file = 'DB3.csv'
lines = open(input_file, "r", encoding="utf_8_sig").readlines()
lines = [line.strip() for line in lines]

# 获取键值
keys = lines[0].split(',')

line_num = 1
total_lines = len(lines)

parsed_datas = []
while line_num < total_lines:
        values = lines[line_num].split(",")
        # parsed_datas.append(dict(zip(keys, values)))
        # parsed_datas.append(dict(zip(line_num, str(dict(zip(keys, values))))))
        parsed_datas.append(str(line_num)+':')
        parsed_datas.append(dict(zip(keys, values)))
        line_num = line_num + 1

json_str = json.dumps(parsed_datas, ensure_ascii=False, indent=4)
output_file = input_file.replace("csv", "json")

# write to the file
f = open(output_file, "w", encoding="utf-8")
f.write(json_str)
f.close()

print("解析结束！")
