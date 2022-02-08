from cProfile import label
import json
with open("task5.json","r")as f:
    data=json.load(f)
def analyse_movie_language():
    language_dict={}
    for i in data:
        if "Language" in i:
            a=i["Language"]
            for i in a:
                if i not in language_dict:
                    language_dict[i]=1
                else:
                    language_dict[i]+=1     
    with open("task6.json","w+") as language_data:
        json.dump(language_dict,language_data,indent=4)
    # print(language_dict)
analyse_movie_language()

