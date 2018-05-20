##  This script is for crawling snapshots from www.mdottraffic.com in Mississippi  

## import necessary libraries 
from bs4 import BeautifulSoup
import os, urllib.request
import re
import time

## save snapshots 
def saveimages(imageurl,folder):
    # request and open imageurl to get image data
    data = urllib.request.urlopen(imageurl).read()
    # make up image file name with folder name and time stamp 
    fileName =folder  + '-'+time.strftime("%c")+'.jpg'
    # make up folder path
    path = '/home/syuan/reptiles/imgs_Miss/'+folder
    # judge if path is exist, or make directory 
    if (not os.path.isdir(path)):
        os.mkdir(path)
    # join one or more path components
    filePath = os.path.join(path, fileName)
    # open image file for writing in binary mode
    image = open(filePath,'wb')
    # wrting data
    image.write(data)clear
    # close image file
    image.close()

## parse weburl to get snapshots stream url, the location is the station name
def getStream(weburl,location):
    # remove space character in the location string
    foldername = location.replace(" ","")
    # request and open weburl 
    content = urllib.request.urlopen(weburl).read()
    # make a soup that is BeautifulSoup object
    soup = BeautifulSoup(content,"html.parser")
    # find all the 'a' tags
    for link in soup.find_all('a'):
        # if the 'a' tags' title equally the location that we want, use re.search to grab its snapshots url
        if (link.get('title') == location):
            image_url = re.search("(?P<url>https?://[^\s]+stream)", link.get('onclick')).group("url")
            # save snapshots  
            saveimages(image_url, foldername) 
            break

## beginning function 
def start(starttime, endtime, intval):
    # wait starttime
    while (time.strftime("%c") < starttime):
        time.sleep(1)
    # make function running until endtime
    while (time.strftime("%c") < endtime):
        getStream('https://www.mdottraffic.com/mapbubbles/camerasite.aspx?site=37','US 90 at Bay St Louis')
        getStream('https://www.mdottraffic.com/mapbubbles/camerasite.aspx?site=75','US 90 West at I-110')
        getStream('https://www.mdottraffic.com/mapbubbles/camerasite.aspx?site=148','US 90 East at Debuys Rd')
        #   getStream('https://streaming5.mdottraffic.com/snapshots?application=rtplive&snap=050204.stream','49_Gulfport')
        getStream('https://www.mdottraffic.com/mapbubbles/camerasite.aspx?site=237','I-10 East at Pascagoula River Bridge')
        #   getStream('https://streaming5.mdottraffic.com/snapshots?application=rtplive&snap=052605.stream','Ponce_De_Leon')
        getStream('https://www.mdottraffic.com/mapbubbles/camerasite.aspx?site=24','US 90 West of MS 609')
        getStream('https://www.mdottraffic.com/mapbubbles/camerasite.aspx?site=114','US 90 West of High Rise Bridge')
        getStream('https://www.mdottraffic.com/mapbubbles/camerasite.aspx?site=113','Jerry St Pe Hwy North of USS Vicksburg Way - Ingalls')
        getStream('https://www.mdottraffic.com/mapbubbles/camerasite.aspx?site=245','MS 57 North at US 90')
        # make processes sleep
        time.sleep(intval*60)

        
## start this script     
## input startdatetime and enddatetime using format like: ’Thu Oct 19 21:56:36 2017‘
## for example: start('Fri Oct 20 10:55:00 2017','Fri Oct 21 10:55:00 2017','10')
start('startdatetime','enddatetime','interval')





    

