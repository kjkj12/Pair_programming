import base64
import json
import os
import requests

from getImage import check

path = "question/"
data = {"teamid": 1, "token": "123afafabbbcc266"}


def request(url):
    response = requests.post(url, data)
    jsons = json.loads(response.text)
    imgData = base64.b64decode(jsons.get('img'))
    file = open(path, 'wb')
    file.write(imgData)
    file.close()
    ls = check(path)
    return ls, jsons.get("swap"), jsons.get("step"), jsons.get('uuid')


if __name__ == '__main__':

    filePath = 'test.jpg'
    baseUrl = "http://47.102.118.1:8089/api/"
    listUrl = baseUrl + "/challenge/list"
    questionUrl = baseUrl + "/challenge/start/"
    submitUrl = baseUrl + "/challenge/submit/"

    qs = requests.get(baseUrl)
    qs = list(qs)
    for q in qs:
        q = json.load(q)
        uuid = q["uuid"]
        path += uuid
        qUrl = questionUrl + uuid
        sUrl = submitUrl + uuid
        l, swap, step, uuid = request(qUrl)

        cpp = "algorithm.exe "
        s = ""

        for i in range(9):
            s += str(l[i])
            s += " "
        s = s + str(step) + " " + str(swap[0]) + " " + str(swap[1])

        cpp += s

        f = os.popen(cpp)
        date = f.readlines()
        f.close()

        result = date[0] if not date else ""

        results = result.split(",")

        answer = {"operations": results[0]}

        swap = []

        if results.__len__() == 3:
            swap.append(int(results[1]))
            swap.append(int(results[2]))

        answer["swap"] = swap

        data["answer"] = answer

        requests.post(sUrl, data)
