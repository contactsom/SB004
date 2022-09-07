#import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
base_url = "https://www.consumeraffairs.com/food/dominos.html"
all_pages_reviews =[]
f = open("Dominos.txt", 'a')
def scraper():
    for i in range(1,6): # fetching reviews from five pages
        query_parameter = "?page="+str(i)
        url = base_url + query_parameter
        response = requests.get(url)
        print("Writing Review For ",url)
        soup = bs(response.content, 'html.parser')
        rev_div = soup.findAll("div",attrs={"class","rvw-bd"})

        for j in range(len(rev_div)):
            pagewise_reviews = None
            pagewise_reviews=rev_div[j].find("p").text
            f.write(pagewise_reviews)
            f.write("\n")

    return all_pages_reviews

reviews = scraper()
print("All Review Captured in file Dominos.txt ")
f.close()
