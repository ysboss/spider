from bs4 import BeautifulSoup
#import os, urllib.request
import os, urllib, requests
import time
import pathlib

## raleigh, NC

def saveimages(url,location):
    #data = urllib.request.urlopen(url).read()
    locDir = 'images/' + location
    if not os.path.exists(locDir):
        os.makedirs(locDir)
        
    try: 
        data = requests.get(url).content
        filePath = locDir + '/' + location + time.strftime("%d-%m-%Y-%H-%M-%S") + '.jpg'
        image = open(filePath,'wb')
        image.write(data)
        image.close()
    except Exception as ex_results:
        print ('Error: ', ex_results)
            
    pass


# revise test
def start():
    for gap in range(100000):
        
        # https://www.floridasforgottencoast.com/things-to-see-do/webcams
        # saveimages('http://50.81.238.92:8150/live/1/mjpeg.jpg?v=1215560469','Carrabelle')
        # saveimages('http://216.227.17.195/live/1/mjpeg.jpg?v=1845965348','Apalachicola')
        
        saveimages('https://fl511.com/map/Cctv/dh54j5sgupk--1','US-98_Tyndall_Parkway_and_Ivy_Rd')
        
        saveimages('https://fl511.com/map/Cctv/txwykx3qf3b--1', 'SR-79_at_SR-388')
        
        saveimages('https://fl511.com/map/Cctv/jhmskawahcm--1','US-89_PCB_Parkway_at_SR-79')
        
        saveimages('https://fl511.com/map/Cctv/55inktek1wg--1','SR-30_Front_Beach_Rd_at_Richard_Jackson_Blvd')      
        
        saveimages('https://fl511.com/map/Cctv/iuxymhewu0h--1','US-98_on_Hathaway_Bridge')        
        
        saveimages('https://fl511.com/map/Cctv/j05xb3mawoo--1','SR-77_at_CR-2302_Ball_Park_Road')
        
        saveimages('https://fl511.com/map/Cctv/1zcct330v0h--1','US-231_at_US-98_W_15th_Street')
        
        # none
        saveimages('https://fl511.com/map/Cctv/pv5fwmxyxzn--1','US-231_at_SR-77_MLK_Jr_Blvd')
        
        # none
        saveimages('https://fl511.com/map/Cctv/kmy5eq3gono--1','US-231_at_N_East_Avenue')
        
        saveimages('https://fl511.com/map/Cctv/fnu0boxzefl--1','US-231_at_Transmitter_Road')
        
        saveimages('https://fl511.com/map/Cctv/sasv1zikkdn--1','US-213_at_CR-390')
        
        saveimages('https://fl511.com/map/Cctv/364--15','US231_MM11_Penny_Rd')
        
        saveimages('https://fl511.com/map/Cctv/365--15','US231_MM13_Johnny_Ln')
        
        saveimages('https://fl511.com/map/Cctv/366--15','US231_MM15_Campflowers_Rd')
        
        saveimages('https://fl511.com/map/Cctv/367--15','US231_MM18_Waller_Rd')
        
        saveimages('https://fl511.com/map/Cctv/368--15','US231_MM21')

        saveimages('https://fl511.com/map/Cctv/369--15','US231_MM22_Linger_Longer_Rd')
        
        saveimages('https://fl511.com/map/Cctv/370--15','US231_MM24_SR-20')
        
                 
        time.sleep(300)
                 
    

start()