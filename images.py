from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

def StartSearch():
    search = input("search for:")
    dir_name = search.replace(" ", "_").lower()
    url = "https://www.bing.com/images/search?q=" + search

    r = requests.get(url)

    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)

    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})

    i = 0

    for item in links:
        try:
            img_ob = requests.get(item.attrs["href"])
            print("Getting", item.attrs["href"])
            title = item.attrs["href"].split("/")[-1]
            try:
                img = Image.open(BytesIO(img_ob.content))
                img.save("./" + dir_name + "/" + title, img.format)
            except:
                print("Could not save image")
            i += 1
            if i == 10:
                break
        except:
            print("could not request image")

    choice =int(input("\n1.Search again\n2.Quit"))
    
    if choice == 1:
        StartSearch()
    else:
        print("Thank You")

StartSearch()
