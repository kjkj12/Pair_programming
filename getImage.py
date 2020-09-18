import base64
import requests
import json


def request(url, path):
    response = requests.get(url)
    jsons = json.loads(response.text)
    imgData = base64.b64decode(jsons.get('img'))
    file = open(path, 'wb')
    file.write(imgData)
    file.close()
    return jsons.get("swap"), jsons.get("step"), jsons.get('uuid')