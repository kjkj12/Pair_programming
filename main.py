from PIL import Image
import os

from ImageCompare import compare_images
from getImage import request


def check():
    f = Image.open("test.jpg")

    base = 300
    fp = which_file(f)
    list = []

    for i in range(3):
        for j in range(3):
            box = (base * j, base * i, base * (j + 1), base * (i + 1))
            region = f.crop(box)

            if is_zero(region):
                list.append(0)
            else:
                s = number(region, fp)
                list.append(s)

    return list


def number(re, fp):
    base = 300
    f = Image.open(fp)
    for i in range(3):
        for j in range(3):
            box = (base * j, base * i, base * (j + 1), base * (i + 1))
            region = f.crop(box)

            if compare_images(re, region):
                return i * 3 + j + 1


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
            return path + '/' + file


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


if __name__ == '__main__':
    filePath = 'test.jpg'
    url = "http://47.102.118.1:8089/api/problem?stuid=031802230"
    swap, step, uuid = request(url, filePath)

    l = check()

    print(l)
    print(step)
    print(swap)
    print(uuid)
