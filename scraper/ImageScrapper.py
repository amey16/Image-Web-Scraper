from bs4 import BeautifulSoup as bs
import os
import json
import requests
import urllib.request
import urllib.parse
import urllib.error
from urllib.request import urlretrieve

header = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
class ImageScrapper:
    
    ## Create  Image URl
    def createImageUrl(searchterm):
        searchterm=searchterm.split()
        searchterm="+".join(searchterm)
        web_url="https://www.google.co.in/search?q=" + searchterm + "&source=lnms&tbm=isch"
        return web_url
    
   # get Raw HTML
    def scrap_html_data(url,header):
        request=urllib.request.Request(url,headers=header)
        response = urllib.request.urlopen(request)
        responseData = response.read()
        html = bs(responseData, 'html.parser')
        return html
    
    # contains the link for Large original images, type of  image
    def getimageList(rawHtml):
        imageUrlList = []
        for a in rawHtml.find_all("img", {"class": "rg_i Q4LuWd"}):
            try:
                link = a['data-src']
                imageUrlList.append(link)
            except KeyError:
                continue

        print("there are total", len(imageUrlList), "images")
        return imageUrlList
    
    def download(imageList,name):
        count=0
        masterlist = []
        imagefiles = []
        for i,link in enumerate(imageList):
            try:
                if (count > 5):
                    break
                else:
                    count = count + 1    
                response = requests.get(link)

                if not os.path.exists('./static'):
                    os.makedirs('./static')
                image_path = './static/' + name + str(i+1) + '.jpg'
                
                with open(image_path,'wb') as f:
                    f.write(response.content)
                
                imagefiles.append(response.content)
            except Exception as e:
                print("could not load :" + link)
                print(e)
                count = count+1
        masterlist.append(imagefiles)

        return masterlist

    def downloaded(self,list_of_images):
        for self.image in list_of_images:
            try:
                os.remove("./static/"+self.image)
            except Exception as e:
                print('error in deleting:  ',e)
        return 0    