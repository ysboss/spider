from bs4 import BeautifulSoup
#import os, urllib.request
import os, urllib, requests
import time
import pathlib


#def saveimages(url,location):
def saveimages(url,location):
    t = time.strftime("%c")
    fileName = location + '-'+t.replace(" ","_")+'.mp4'
    path = '/home/syuan/reptiles/north_carolina/images3/'+location
    pathlib.Path(path).mkdir(parents=True, exist_ok=True) 
    cmd = 'ffmpeg -i $(youtube-dl -f 95 -g '+url+') -c:v copy -c:a aac -strict experimental -t 00:00:05 '+path+'/'+fileName
    #print (cmd)
    os.system(cmd)
    
def start():
    for gap in range(100000):
        saveimages('https://www.youtube.com/watch?v=a-gJoO9A6so','Sharks_in_the_Atlantic')
        saveimages('https://www.youtube.com/watch?v=deG4NxkouGM','Frying_Pan_Tower')
        saveimages('https://www.youtube.com/watch?v=ZENO8e6IITA','Sky_Tower_in_Wilmington')
        saveimages('https://www.youtube.com/watch?v=BKOtfXySLEk','Outer_Banks_Beach')
        
        time.sleep(600)
start()

