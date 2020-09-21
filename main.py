from getImage import ImageDeal

if __name__ == '__main__':
    filePath = 'test.jpg'
    url = "http://47.102.118.1:8089/api/problem?stuid=031802230"
    l, swap, step, uuid = ImageDeal(url, filePath)

    print(l)
    print(step)
    print(swap)
    print(uuid)
