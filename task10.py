from multiprocessing.spawn import import_main_path
import json
with open("task5.json","r")as f:
    data=json.load(f)
def nalyse_language_and_directors():
    m=[]
    for i in data:
        pt=i["Director"]
        for i in pt:
            if i not in m:
                m.append(i)
    dic={}
    for y in m:
        dict1={}
        for x in data:
            if "Language" in x:
                for z in x["Language"]:
                    if z is dict1:
                        dict1[z]+=1
                    if z not in dict1:
                        dict1[z]=1
        dic[y]=dict1
    with open("task10.json","w+") as file:
      json.dump(dic,file,indent=4)
nalyse_language_and_directors()