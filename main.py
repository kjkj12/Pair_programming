import os
from getImage import ImageDeal
from sendResult import send

if __name__ == '__main__':

    filePath = 'test.jpg'
    url = "http://47.102.118.1:8089/api/problem?stuid=031802604"
    l, swap, step, uuid = ImageDeal(url, filePath)

    # l = [4, 0, 1, 7, 5, 8, 6, 9, 2]
    # step = 19
    # swap = [9, 5]
    # uuid = "03daec369b5e434583b48445113ef409"

    print(l)
    print(step)
    print(swap)
    print(uuid)

    cpp = "algorithm.exe "
    s = ""

    for i in range(9):
        s += str(l[i])
        s += " "
    s = s + str(step) + " " + str(swap[0]) + " " + str(swap[1])

    cpp += s

    f = os.popen(cpp)
    data = f.readlines()
    f.close()

    print(data[0])

    send(uuid, data[0])
