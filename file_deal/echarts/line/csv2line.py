#! python3
# -*- coding:utf-8 -*-


def csv2dic(input_csv):
    with open(input_csv, "r", encoding="utf_8_sig") as f:
        lines = f.readlines()
    lines = [line.split(',') for line in lines]
    keys = []
    values = []
    for line in lines:
        keys.append(line[0])
        values.append(float(line[1].strip()))

    return (keys, values)


def deal_html(input_html, xAxis, yAxis):
    with open(input_html, "r", encoding="utf_8_sig") as f:
        content = f.read()

    data_x = csv2dic(input_csv)[0]
    data_y = csv2dic(input_csv)[1]
    new_x = "data: ["
    new_y = "data: ["
    for i in range(len(data_x)):
        new_x += (str(data_x[i]) + ', ')
        new_y += (str(data_y[i]) + ', ')
    new_x += ']'
    new_y += ']'

    new_cont = content.replace(xAxis, new_x)
    new_cont = new_cont.replace(yAxis, new_y)

    with open(input_html.replace('.html', '_new.html'), "w", encoding="utf_8_sig") as f:
        f.write(new_cont)


if __name__ == '__main__':
    input_csv = '河流流量.csv'
    input_html = 'line-simple.html'
    xAxis = r"data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']"
    yAxis = r"data: [820, 932, 901, 934, 1290, 1330, 1320]"
    deal_html(input_html, xAxis, yAxis)
    print("解析结束！")
