from bs4 import BeautifulSoup
#import os, urllib.request
import os, urllib, requests
import time
import pathlib

    

def saveimages(url,location):
    #data = urllib.request.urlopen(url).read()
    data = requests.get(url).content
    fileName = location + '-'+time.strftime("%c")+'.jpg'
    path = '/home/syuan/reptiles/north_carolina/images4/'+location
    pathlib.Path(path).mkdir(parents=True, exist_ok=True) 
    filePath = os.path.join(path, fileName)
    image = open(filePath,'wb')
    image.write(data)
    image.close()
# revise test
def start():
    for gap in range(100000):
        saveimages('https://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=I95NB_NC211LumbertonMM20.jpg','MM20')
        saveimages('https://tims.ncdot.gov/TIMS/Cameras/viewimage.ashx?id=US301_Wintergreen_St.jpg','US301_Wintergreen_St')
        saveimages('https://tims.ncdot.gov/TIMS/Cameras/viewimage.ashx?id=I95_US301_Exit33.jpg','I95_US301_Exit33')
        saveimages('https://tims.ncdot.gov/TIMS/Cameras/viewimage.ashx?id=I95_Wade-Stedman_Rd.jpg','I95_Wade-Stedman_Rd')         
        saveimages('https://tims.ncdot.gov/TIMS/Cameras/viewimage.ashx?id=I95NB_US421DunnMM73.jpg','I95NB_US421DunnMM73')        
        saveimages('https://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=I95_mm79.jpg','I95_mm79')
        saveimages('https://tims.ncdot.gov/TIMS/Cameras/viewimage.ashx?id=I95_Keen_Rd.jpg','I95_Keen_Rd')
        saveimages('https://tims.ncdot.gov/TIMS/Cameras/viewimage.ashx?id=NC24_Plantation_Dr.jpg','NC24_Plantation_Dr')
                 
        time.sleep(600)
                 
    

start()