# import json
# from task1 import year_l                        
# f=open("task2.json","r")
# data1=json.load(f)
# print(data1) 
from bs4 import BeautifulSoup
import json
file1 = open("task1.json")
movies = json.load(file1)
decade_dic={"1930":[],"1940":[],"1950":[],"1960":[],"1970":[],"1980":[],"1990":[],"2000":[],"2010":[],"2020":[]}
def decade_by_year(movies):
    for i in movies:
        if i["Release"]>=1930 and i["Release"]<1940:
            decade_dic["1930"].append(i)
        elif i["Release"]>=1940 and i["Release"]<1950:
            decade_dic["1940"].append(i)
        elif i["Release"]>=1950 and i["Release"]<1960:
            decade_dic["1950"].append(i)
        elif i["Release"]>=1960 and i["Release"]<1970:
            decade_dic["1960"].append(i)
        elif i["Release"]>=1970 and i["Release"]<1980:
            decade_dic["1970"].append(i)
        elif i["Release"]>=1980 and i["Release"]<1990:
            decade_dic["1980"].append(i)
        elif i["Release"]>=1990 and i["Release"]<2000:
            decade_dic["1990"].append(i)
        elif i["Release"]>=2000 and i["Release"]<2010:
            decade_dic["2000"].append(i)
        elif i["Release"]>=2010 and i["Release"]<2020:
            decade_dic["2010"].append(i)
        elif i["Release"]>=2020 and i["Release"]<2030:
            decade_dic["2020"].append(i)

    with open("task3.json","w+")as file3:
        json.dump(decade_dic,file3,indent=4)
        # a=json.dumps(decade_dic)
        return decade_dic
decade_by_year(movies) 