import json
import requests
URL = "https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/"
sample = requests.get(URL)
from bs4 import BeautifulSoup
soup = BeautifulSoup(sample.text,"html.parser")
def movie_data() :
    l=[]
    title=soup.find("div",class_="panel-body content_body allow-overflow")
    table=title.find("table",class_="table")
    tr=table.find_all("tr")
    for i in tr:
        dic={}
        td=i.find_all("td")
        for k in td:
            rank=i.find("td",class_="bold").text[:-1]
            rating=i.find("span",class_="tMeterIcon tiny").text[-4:-2]
            name=i.find("a",class_="unstyled articleLink")["href"][3:]
            reviews=i.find("td",class_="right hidden-xs").text
            release=i.find("a",class_="unstyled articleLink").get_text()
            Release=release.strip()
            movie_url=i.find("a",class_="unstyled articleLink")["href"]
            url="https://www.rottentomatoes.com"+movie_url
            dic["Rank"]=int(rank)
            dic["Rating"]=float(rating)
            dic["name"]=(name)  
            dic["Reviews"]=int(reviews)
            dic["Release"]=int(Release[-5:-1])
            dic["url"]=(url)
        l.append(dic)
        if {} in l :
            l.remove({})
    with open("task1.json","w+")as file:
        json.dump(l,file,indent=4)
        return l
movie_data()