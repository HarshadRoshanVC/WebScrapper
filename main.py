from bs4 import BeautifulSoup
import requests

search = input("Enter search term:")
params = {"q": search}
r = requests.get("https://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")

result = soup.find("ol",{"id": "b_results"})
links = result.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)
        #print("Parent:", item.find("a").parent)
        #print("Summery:", item.find("a").parent.parent.find("p").text + "\n")

        children = item.find("h2")
        #for child in children:
            #print("Child:",child)
        print("Next sibling of the h2:", children.next_sibling)