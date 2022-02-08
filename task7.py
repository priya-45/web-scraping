import json
with open("task5.json","r")as f:
    data=json.load(f)
def analyse_movie_director():
    director_dict={}
    for i in data:
        if "Director" in i:
            a=i["Director"]
            i=0
            b=[]
            while i<len(a):
                c=a[i].replace(' ','')
                b.append(c)
                i=i+1
            print(b)
            for j in b:
                if j not in director_dict:
                    director_dict[j]=1
                else:
                    director_dict[j]+=1
        else:
            pass     
    with open("task7.json","w+") as language_data:
        json.dump(director_dict,language_data,indent=4)
analyse_movie_director()