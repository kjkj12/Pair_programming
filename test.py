import json
import os
import time
import traceback

if __name__ == '__main__':
    i = 1
    k = 1
    while True:
        try:
            f = os.popen("python main.py")
            data = f.readlines()
            j = json.loads(data[-2][:-1])
            if not j["score"]:
                print(j["time"])
                print("error   "+str(i))
                with open('error/'+str(i)+'.txt', mode="w") as f:
                    f.write("".join(data))
                i += 1
            else:
                print(j["time"])
                print("success "+str(k))
                with open('success/'+str(k)+'.txt', mode="w") as f:
                    f.write("".join(data))
                k += 1
        except Exception as e:
            print("========================================================================")
            print('traceback.format_exc():\n%s' % traceback.format_exc())
        finally:
            time.sleep(1)
