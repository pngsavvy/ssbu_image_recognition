#!/usr/bin/python
from PIL import Image
import os, sys

path = "C:\\Projects\\pekpek-savvy\\Screenshots\\Attacks\\Jab\\Shield\\"
hsv_jab = "C:\\Projects\\pekpek-savvy\\Screenshots\\HSV_Mario_Training\\Attacks\\Jab"
hsv_grab = "C:\\Projects\\pekpek-savvy\\Screenshots\\HSV_Mario_Training\\Grab"
hsv_jump = "C:\\Projects\\pekpek-savvy\\Screenshots\\HSV_Mario_Training\\Jump"
hsv_neutral_special = "C:\\Projects\\pekpek-savvy\\Screenshots\\HSV_Mario_Training\\Specials\\Neutral Special"

dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((1904,1042), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=60)
            print(item)

            if os.path.isfile(item):
                os.remove(item)
            else:    ## Show an error ##
                print("Error: %s file not found" % item)

    '''
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((1904,1042), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=60)
    
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((1904,1042), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=60)
    
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((1904,1042), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=60)
    '''

resize()