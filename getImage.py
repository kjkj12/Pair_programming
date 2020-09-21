import base64
import os

import requests
import json

from PIL import ImageChops, Image


def request(url, path):
    response = requests.get(url)
    jsons = json.loads(response.text)
    imgData = base64.b64decode(jsons.get('img'))
    file = open(path, 'wb')
    file.write(imgData)
    file.close()
    return jsons.get("swap"), jsons.get("step"), jsons.get('uuid')


def compare_images(image_one, image_two):
    try:
        diff = ImageChops.difference(image_one, image_two)

        if diff.getbbox() is None:
            # 图片间没有任何不同则直接退出
            return True
        else:
            return False

    except ValueError as e:
        return "{0}\n{1}".format(e, "图片大小和box对应的宽度不一致!")


def check():
    f = Image.open("test.jpg")
    for f in which_file(f):
        lists = getList(f)
        if lists.__len__() == 9:
            return lists


def getList(fp):
    f = Image.open("test.jpg")
    base = 300
    lists = list()
    for i in range(3):
        for j in range(3):
            box = (base * j, base * i, base * (j + 1), base * (i + 1))
            region = f.crop(box)

            if is_zero(region):
                lists.append(0)
            else:
                s = number(region, fp)
                if s == 10:
                    return lists
                lists.append(s)

    return lists


def number(re, fp):
    base = 300
    f = Image.open(fp)
    for i in range(3):
        for j in range(3):
            box = (base * j, base * i, base * (j + 1), base * (i + 1))
            region = f.crop(box)

            if compare_images(re, region):
                return i * 3 + j + 1

    return 10


def which_file(f):
    path = 'Images'

    box_1 = (0, 0, 300, 300)
    box_2 = (0, 300, 300, 600)
    region = f.crop(box_1)
    if is_zero(region):
        region = f.crop(box_2)

    files = os.listdir(path)
    for file in files:
        if is_in(path + '/' + file, region):
            print(file)
            yield path + '/' + file


def is_in(fp, r):
    base = 300

    f = Image.open(fp)

    for i in range(3):
        for j in range(3):
            box = (base * i, base * j, base * (i + 1), base * (j + 1))
            region = f.crop(box)
            if compare_images(region, r):
                return fp


def is_zero(region):
    space = Image.open("space.jpg")
    if compare_images(space, region):
        return True
    else:
        return False


def ImageDeal(url, filePath):
    swap, step, uuid = request(url, filePath)
    l = check()
    return l, swap, step, uuid
