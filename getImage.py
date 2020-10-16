import base64
import os

import imagehash
import requests
import json

from PIL import Image
from PIL.ImageFile import ImageFile


def request(url, path):
    response = requests.get(url)
    jsons = json.loads(response.text)
    imgData = base64.b64decode(jsons.get('img'))
    file = open(path, 'wb')
    file.write(imgData)
    file.close()
    return jsons.get("swap"), jsons.get("step"), jsons.get('uuid')


def compare_images(image_one, image_two, max_dif=0):
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    hash_1 = imagehash.average_hash(image_one)
    hash_2 = imagehash.average_hash(image_two)
    dif = hash_1 - hash_2
    if dif < 0:
        dif = -dif
    if dif <= max_dif:
        return True
    else:
        return False


def check(path="test.jpg"):
    f = Image.open(path)
    for ls in which_file(f):
        lists = getList(ls, path)
        if lists.__len__() == 9:
            print(ls)
            return lists


def getList(fp, path="test.jpg"):
    f = Image.open(path)
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
