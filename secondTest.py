import json

import requests

data = {"teamid": "11", "token": "67958336-8e43-472b-9e44-018280aad0bb"}
url = "http://47.102.118.1:8089/api/challenge/start/" + "c996219f-82dc-42b9-8f17-9f65d6512b3b"
submitUrl = "http://47.102.118.1:8089/api/challenge/submit"
formdata = {"uuid": "", "teamid": "11", "token": "67958336-8e43-472b-9e44-018280aad0bb"}
header = {'Content-Type': 'application/json', "charset": "UTF-8"}

if __name__ == '__main__':

    answer = {"operations": "", "swap": []}
    formdata["answer"] = answer
    response = requests.post(url, json=data)
    jsons = json.loads(response.text)
    tmp = jsons.get("uuid")
    formdata["uuid"] = tmp

    responses = requests.post(submitUrl, json=formdata)
    print(responses.text)
