import os
from getImage import ImageDeal

if __name__ == '__main__':

    filePath = 'test.jpg'
    url = "http://47.102.118.1:8089/api/problem?stuid=031802230"
    l, swap, step, uuid = ImageDeal(url, filePath)

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
