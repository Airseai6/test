#! python3
# -*- coding:utf-8 -*-

import qrcode
from io import BytesIO
import base64

def gen_qrcode(content):
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4)
    '''
    version：值为1~40的整数，控制二维码的大小（最小值是1，是个12×12的矩阵）。 如果想让程序自动确定，将值设置为 None 并使用 fit 参数即可。
    
    error_correction：控制二维码的错误纠正功能。可取值下列4个常量。
    　　ERROR_CORRECT_L：大约7%或更少的错误能被纠正。
    　　ERROR_CORRECT_M（默认）：大约15%或更少的错误能被纠正。
    　　ROR_CORRECT_H：大约30%或更少的错误能被纠正。
    
    box_size：控制二维码中每个小格子包含的像素数。
    
    border：控制边框（二维码与图片边界的距离）包含的格子数（默认为4，是相关标准规定的最小值）
    '''
    qr.add_data(content)
    qr.make(fit=True)
    img = qr.make_image()
    # img.save('qrcode_temp.png')

    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue())
    return img_str


if __name__ == '__main__':
    content = 'Hello, 你好！'
    gen_qrcode(content)
    from PIL import Image
    im = Image.open('qrcode_temp.png')
    im.show()