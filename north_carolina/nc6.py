from bs4 import BeautifulSoup
#import os, urllib.request
import os, urllib, requests
import time
import pathlib

## raleigh, NC

def saveimages(url,location):
    #data = urllib.request.urlopen(url).read()
    data = requests.get(url).content
    fileName = location + '-'+time.strftime("%c")+'.jpg'
    path = '/home/syuan/reptiles/north_carolina/images6/'+location
    pathlib.Path(path).mkdir(parents=True, exist_ok=True) 
    filePath = os.path.join(path, fileName)
    image = open(filePath,'wb')
    image.write(data)
    image.close()
# revise test
def start():
    for gap in range(100000):
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=40_Rock_Quarry.JPG','I-40_Rock_Quarry_Rd')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=40_Saunders.JPG','I-40_S_Saunders_St')
        saveimages('https://tims.ncdot.gov/TIMS/Cameras/viewimage.ashx?id=64_Arendell.JPG','US_64_Arendell_Ave')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=i-440-wade.jpg','I-440_Wade_Ave')      
        
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=oldmilburn.jpg','US_64_Old_Milburnie_Rd')        
        
        saveimages('https://tims.ncdot.gov/TIMS/cameras/viewimage.ashx?id=US1_mm97.jpg','US_1_mm_97')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=gleneden.jpg','Edwards_Mill_Rd_Glen_Eden_Dr')
        
        saveimages('https://tims.ncdot.gov/TIMS/Cameras/viewimage.ashx?id=I95_NC42.jpg','I95_at_NC_42')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=I-40_Cleveland_Rd.jpg','I-40_WB_Cleveland_Rd')
        
        saveimages('https://tims.ncdot.gov/TIMS/Cameras/viewimage.ashx?id=85_Red_Mill.JPG','I-85_Red_Mill_Rd')
    
                 
        time.sleep(600)
                 
    

start()