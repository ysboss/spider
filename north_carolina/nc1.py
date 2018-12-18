from bs4 import BeautifulSoup
#import os, urllib.request
import os, urllib, requests
import time
import pathlib

    

def saveimages(url,location):
    #data = urllib.request.urlopen(url).read()
    data = requests.get(url).content
    fileName = location + '-'+time.strftime("%c")+'.jpg'
    path = '/home/syuan/reptiles/north_carolina/images/'+location
    pathlib.Path(path).mkdir(parents=True, exist_ok=True) 
    filePath = os.path.join(path, fileName)
    image = open(filePath,'wb')
    image.write(data)
    image.close()
# revise test
def start():
    for gap in range(100000):
        saveimages('http://gray.ftp.clickability.com/witnwebftp/webcams/mhcsc.jpg','MoreheadCity')
        saveimages('http://gray.ftp.clickability.com/witnwebftp/webcams/rivercam.jpg','Washington')
        saveimages('http://gray.ftp.clickability.com/witnwebftp/webcams/neuse.jpg','NeuseRiver')
        saveimages('http://gray.ftp.clickability.com/witnwebftp/webcams/nbcam.jpg','NewBern')
        time.sleep(600)
    

start()