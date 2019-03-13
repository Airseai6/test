#! python3
# -*- coding:utf-8 -*-
import aircv as ac
from PIL import Image
import PIL.ImageOps


def invert_img(imgobj):
    # 读入图片
    image = Image.open(imgobj)
    # 反转颜色
    inverted_image = PIL.ImageOps.invert(image)
    # 保存图片
    inverted_image.save(imgobj.replace('.', '_i.'))


def deal_img(imgsrc, imgobj, location):
    # 读入图片
    image = Image.open(imgsrc)
    # 处理翻转图片
    obj1 = Image.open(imgobj)
    # obj = ac.imread(imgobj)
    # r, g, b, a = obj1.split()
    # obj1.convert('RGBA')
    # 用翻转的图片覆盖已查找位置
    # image.paste(obj1, location, mask=a)
    image.paste(obj1, location)
    # 保存图片
    # image.save(imgsrc.replace('.', '_temp.'))
    image.save(imgsrc)
    # w, h = obj.size
    # new = Image.new('RGB', (w, h), 'white')
    # image.paste(new, location)
    # image.save(imgsrc)


def matchImg(imgsrc, imgobj, confidence=0.5):
    """
    imgsrc=原始图像，imgobj=待查找的图片, confidence=0.5, 默认最低相似率
    返回结果为一个字典：
    {'result': (155.0, 82.0), 'rectangle': ((135, 52), (135, 112), (175, 52), (175, 112)),
    'confidence': 1.0, 'shape': (682, 549)}

    result：匹配图片在原始图片上的中心坐标点
    rectangle：匹配图片在原始图像上四边形的坐标
    confidence：匹配相似率
    shape：原图宽*高
    """
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)
    match_result = ac.find_template(imsrc, imobj, confidence)
    if match_result is not None:
        match_result['shape'] = (imsrc.shape[1], imsrc.shape[0])  # 0为高，1为宽

    return match_result


def main(imgsrc, imgobj, confidence):
    result = []
    invert_img(imgobj)
    image = Image.open(imgsrc)
    im_temp = imgsrc.replace('.', '_temp.')
    image.save(im_temp)
    while True:
        find = matchImg(im_temp, imgobj, confidence)
        if find is None:
            break
        if find['result'] not in result:
            result.append(find['result'])
            location = find['rectangle'][0]
            deal_img(im_temp, imgobj.replace('.', '_i.'), location)

    return result


if __name__ == '__main__':
    """
    imgsrc big
    target small
    """
    imgsrc = 'IV-5.png'
    target = 'hep3.bmp'
    r = main(imgsrc, target, 0.4)
    print(len(r))
    print(r)
