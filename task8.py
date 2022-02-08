import requests
from bs4 import BeautifulSoup
import json
import os
from task1 import movie_data
movie = movie_data()
def get_movie_list_details(a):
    for i in a:
        path="/home/dell/Documents/task8/task8"+i["name"]+".text"
        if os.path.exists("file.json"):
            pass
        else:
            create=open(path,"w+")
            url=requests.get(i["url"])
            create.write(url.text)
get_movie_list_details(movie)