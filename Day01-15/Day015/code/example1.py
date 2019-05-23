"""
Pillow

@Author:jyang
@Date:5/22/2019
"""

from PIL import Image

image = Image.open('../res/people.jpg') # BingWallpaper-2019-05-21.jpg

def base():
    print(image.format, image.size, image.mode)
    image.show()

def cut():
    '''
    剪裁图像
    crop()方法可以从图片中提取一个子矩形
    Pillow左边系统的原点（0，0）为图片的左上角。坐标中的数字单位为像素点。
    rect: 该tuple中信息为(left, upper, right, lower)
    :return:
    '''
    rect = 80+100, 20, 310+100, 300
    image.crop(rect).show()

def shrink():
    '''
    生成缩略图
    :return:
    '''
    size = 128, 128
    image.thumbnail(size)
    image.show()

def shrinkCopy():
    '''
    缩放和粘贴图像
    :return:
    '''
    image1 = Image.open('../res/BingWallpaper-2019-05-21.jpg')
    image2 = Image.open('../res/people.jpg')
    rect = 80+100, 20, 310+100, 300
    image2_head = image2.crop(rect) # 截取图2的部分
    # image2_head.show()
    width, height = image2_head.size
    # image2_head.resize((int(width / 1.5), int(height / 1.5)))
    image1.paste(image2_head.resize((int(width/1.5), int(height/1.5))), (230, 280))


if __name__ == '__main__':
    # base()
    # cut()
    # shrink()
    shrinkCopy()