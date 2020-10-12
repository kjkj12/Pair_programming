import base64
import json
import os
import requests
import time

from getImage import check

p = "question/"
path = ""
data = {"teamid": "11", "token": "67958336-8e43-472b-9e44-018280aad0bb"}
datass = {"uuid": "", "teamid": "11", "token": "67958336-8e43-472b-9e44-018280aad0bb"}


def request(url):
    response = requests.post(url, json=data)
    jsons = json.loads(response.text)
    tmp = jsons.get("uuid")
    jsons = jsons.get('data')
    imgData = base64.b64decode(jsons.get('img'))
    file = open(path, 'wb')
    file.write(imgData)
    file.close()
    ls = check(path)
    return ls, jsons.get("swap"), jsons.get("step"), tmp


if __name__ == '__main__':

    time = time.time()
    print(time)

    filePath = 'test.jpg'
    baseUrl = "http://47.102.118.1:8089/api"
    listUrl = baseUrl + "/challenge/list"
    questionUrl = baseUrl + "/challenge/start/"
    submitUrl = baseUrl + "/challenge/submit"

    i = 20
    k = 0
    qs = requests.get(listUrl)
    qs = qs.text
    print(qs)

    qs = json.loads(qs)

    print(qs)
    for q in qs:
        if q["author"] == 11:
            continue
        if q["pubtimestamp"] < 1602516715.5083148:
            continue
        uuid = q["uuid"]

        path = p + uuid + '.jpg'
        qUrl = questionUrl + uuid
        l, swap, step, tid = request(qUrl)

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

        result = date[0] if date else ""

        results = result.split(",")

        answer = {"operations": results[0]}

        swap = []

        if results.__len__() == 3:
            swap.append(int(results[1]))
            swap.append(int(results[2]))

        answer["swap"] = swap

        datass["answer"] = answer

        datass["uuid"] = tid

        responses = requests.post(submitUrl, json=datass)

        j = json.loads(responses.text)
        if not j["success"]:
            print(j["timeelapsed"])
            print("error   " + str(i))
            with open('error/' + str(i) + '.txt', mode="w") as f:
                f.write(responses.text)
                f.write(str(l))
                f.write('\n')
                f.write(result)
                f.write('\n')
                f.write(s)
                f.write('\n')
                f.write(uuid)
            i += 1
        else:
            print(j["timeelapsed"])
            print("success " + str(k))
            with open('success/' + str(k) + '.txt', mode="w") as f:
                f.write(responses.text)
                f.write(str(l))
                f.write('\n')
                f.write(result)
                f.write('\n')
                f.write(s)
                f.write('\n')
                f.write(uuid)
            k += 1
