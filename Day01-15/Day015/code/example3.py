"""
创建缩略图

@Author:jyang
@Date:5/22/2019
"""
from PIL import Image
import os, sys

infile = '../res/BingWallpaper-2019-05-21.jpg'
outfile = os.path.splitext(infile)[0] + "thumbnail.png"
size = (128, 128)
try:
    im = Image.open(infile)
    im.thumbnail(size)
    im.save(outfile, 'PNG')
except IOError:
    print('Cannot create thumbnail for', infile)