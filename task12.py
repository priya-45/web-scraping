# from argparse import Action
import json
from bs4 import BeautifulSoup
import requests
movieurl="https://www.rottentomatoes.com/m/toy_story_4"
movieName="toy_story_4"
def scrape_movie_cast():
    url=requests.get(movieurl)
    data=BeautifulSoup(url.text,"html.parser")
    mainDiv=data.find("div",class_="castSection")
    d1=data.find_all("div",class_="cast-item media inlineBlock")
    d2=data.find_all("div",class_="cast-item media inlineBlock moreCasts hide")
    actor_list=[]
    for i in d1:
        dict1={}
        name=i.find("a")["href"][11:]
        dict1["actor name"]=name
        actor_list.append(dict1)
    for i in d2:
        dict1={}
        name1=i.find("a")["href"][11:]
        dict1["actor name"]=name1
        actor_list.append(dict1)
    with open ("task12.json","w+") as file:
        json.dump(actor_list,file,indent=4)
scrape_movie_cast()
            
            
       