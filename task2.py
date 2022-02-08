import json
# from task1 import movie_data
# data=movie_data()
file=open("task1.json","r")
data=json.load(file)
def year_l():
    d1={}
    for i in data:
        n=[]
        year=i["Release"]
        if year not in d1:
            for key in data:
                if year == key["Release"]:
                    n.append(key)
            d1[year]=n        
    with open("task2.json","w+") as file:
        json.dump(d1,file,indent=4)
        # a=json.dumps(d1)
        return d1
year_l()