import json
import os
import time
import traceback

if __name__ == '__main__':
    i = 1
    while True:
        try:
            f = os.popen("python main.py")
            data = f.readlines()
            j = json.loads(data[-2][:-1])
            if not j["score"]:
                with open(str(i)+'.txt', mode="w") as f:
                    f.write("".join(data))
                i += 1
        except Exception as e:
            print("========================================================================")
            print('traceback.format_exc():\n%s' % traceback.format_exc())
        finally:
            time.sleep(5)
