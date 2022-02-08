# from task4 import scrape_movie_details
# from task12 import scrape_movie_cast
import json
with open ("task4.json","r")as file:
    data=json.load(file)
with open ("task12.json","r")as f:
    data1=json.load(f)
m=[]
def get_movie_list_details():
    print()
    m.append(data)
    m.append(data1)
    # print(m)
    with open("task13.json","w+")as file1:
        json.dump(m,file1,indent=4)
get_movie_list_details()