from task1 import movie_data
import requests
from bs4 import BeautifulSoup
import json
def scrape_movie_details(data1):
    url=requests.get(data1)
    url_details = BeautifulSoup(url.text,"html.parser")
    li=url_details.find_all('li',class_="meta-row clearfix")
    name=url_details.find("h1",class_="scoreboard__title").get_text()
    details={}
    list=[]
    movie=movie_data()
    for i in li:
        k=i.text
        n=k.split()
        # print(n)
        for j in n:
            if "Rating" in j:
                details["name"]=name
                details["Rating"]=n[1]
            if "Genre" in j:
                a=n[1:]
                m=" "
                for i in a:
                    m+=i
                m=m.split(",")
                details["Genre"]=m
            if "Language" in j:
                details["Language"]=n[2:]
            if "Director" in j:
                a=n[1:]
                s=" "
                for i in a:
                    s+=i
                s=s.split(",")
                details["Director"]=s
            if "Producer" in j:
                a=n[1:]
                l=" "
                for i in a:
                    l+=i
                l=l.split(",")
                details["Producer"]=l
            if "Writer" in j:
                a=n[1:]
                v=" "
                for i in a:
                    v+=i
                v=v.split(",")
                details["Writer"]=v
            if "Release" in j:
                details["Release"]=n[3:6]
            if "Runtime" in j:
                time=n[1:]
                # print(time)
                i=0
                while i<len(time):
                    hour=time[0][0]
                    mint=time[1]
                    min=mint[:-1]
                    # print(min)
                    i=i+1
                tom=int(hour)*60+int(min)
                details["Runtime"]=tom
    with open("task4.json","w+")as file:
        json.dump(details,file,indent=4)
        return details
scrape_movie_details("https://www.rottentomatoes.com/m/toy_story_4")
