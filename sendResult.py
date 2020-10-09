import json

import requests

formdata = {}
url = "http://47.102.118.1:8089/api/answer"
header = {'Content-Type': 'application/json', "charset": "UTF-8"}


def send(uuid, result):
    results = result.split(",")
    formdata["uuid"] = uuid

    answer = {"operations": results[0]}

    swap = []

    if results.__len__() == 3:
        swap.append(int(results[1]))
        swap.append(int(results[2]))

    answer["swap"] = swap

    formdata["answer"] = answer

    response = requests.post(url, json=formdata, headers=header)

    print(json.dumps(formdata))
    print(response.text)
