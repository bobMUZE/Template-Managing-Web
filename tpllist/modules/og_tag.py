from bs4 import BeautifulSoup
import requests
import json
import re

def find_og_img(url):
    pass
    # try:
    #     html = requests.post(url)
    #     soup = BeautifulSoup(html.content, "html.parser")

    #     metas = soup.find(property="og:image")

    #     if metas == None:
    #         return "No Image"
    #         imgs = soup.find('img')
    #         return imgs['src']

    #     return metas['content']
    # except:
    #     return "error"
