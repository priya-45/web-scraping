import json
import os
import time
import random
with open("task5.json","r") as file:
    movie=json.load(file)
def movie_list_details():
    random_sleep=random.randint(1,3)
    for i in movie:
        if "name" in i:
            path="/home/dell/Documents/task9/task9"+i["name"]+".json"
        print(path)
        if os.path.exists(path):
            pass
        else:
            a=open(path,"w+")
            # url=requests.get(i)
            json.dump(i,a,indent=4)
        time.sleep(random_sleep)
movie_list_details()