from scrawper.ImageScrapper import ImageScrapper as isc

class BusinessLayer:
    
    keyword=""
    fileLoc=""
    image_name=""
    header=""
     
    def downloadImages(keyWord, header):
        imgScrapper = isc
        url = imgScrapper.createImageUrl(keyWord)
        rawHtml = imgScrapper.scrap_html_data(url, header)
        
        imageURLList = imgScrapper.getimageList(rawHtml)
        
        masterListOfImages = imgScrapper.download(imageURLList,keyWord)
        
        return masterListOfImages    
   