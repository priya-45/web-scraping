import json
from bs4 import BeautifulSoup
from task1 import movie_data
from task4 import scrape_movie_details
movie = movie_data()
# print(movie)
def get_movie_list_details():  
    movie_list = []
    for i in movie:
        url1=i["url"]
        # print(url1)
        a=scrape_movie_details(url1)
        movie_list.append(a)
        print(movie_list)
    with open("task5.json","w+") as file5:
        json.dump(movie_list,file5,indent=4)
get_movie_list_details()
