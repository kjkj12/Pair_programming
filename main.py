from queue import Queue

from Square_Nine import Square
from getImage import ImageDeal

if __name__ == '__main__':

    filePath = 'test.jpg'
    url = "http://47.102.118.1:8089/api/problem?stuid=031802230"
    l, swap, step, uuid = ImageDeal(url, filePath)

    print(l)
    print(step)
    print(swap)
    print(uuid)

    Square.orig = swap[0]
    Square.to = swap[1]
    Square.xth = step

    for i in range(3):
        for j in range(3):
            if l[i * 3 + j] == 0:
                x = i
                y = j

    s = Square(l[0:3], l[3:6], l[6:9], 0, 0, "", x, y)

    used = {s}
    q = Queue()
    q.put(s)
    result = "没有结果"
    while q.qsize() != 0:
        s = q.get()
        if s.isAns():
            result = s.path
            break
        t = s.up_mov()
        if t not in used:
            q.put(t)
            used.add(t)
        t = s.down_mov()
        if t not in used:
            q.put(t)
            used.add(t)
        t = s.left_mov()
        if t not in used:
            q.put(t)
            used.add(t)
        t = s.right_mov()
        if t not in used:
            q.put(t)
            used.add(t)
    print(result)
