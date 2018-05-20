from bs4 import BeautifulSoup
import os, urllib.request
import re
import time

def saveimages(url,location):
    data = urllib.request.urlopen(url).read()
    fileName = location + '-'+time.strftime("%c")+'.jpg'
    path = '/home/syuan/reptiles/imgs_Miss/'+location
    filePath = os.path.join(path, fileName)
    image = open(filePath,'wb')
    image.write(data)
    image.close()
        

def start():
    for gap in range(100000):
        saveimages('https://streaming5.mdottraffic.com/snapshots?application=rtplive&snap=051807.stream','Bay_St_Louis')
        saveimages('https://streaming5.mdottraffic.com/snapshots?application=rtplive&snap=050301.stream','I-110_Biloxi')
        saveimages('https://streaming5.mdottraffic.com/snapshots?application=rtplive&snap=050201.stream','Debuys_Gulfport')
        saveimages('https://streaming5.mdottraffic.com/snapshots?application=rtplive&snap=050204.stream','49_Gulfport')
        saveimages('https://streaming5.mdottraffic.com/snapshots?application=rtplive&snap=051107.stream','I-10_Pascagoula_High_Rise_Bridge')
        saveimages('https://streaming5.mdottraffic.com/snapshots?application=rtplive&snap=052605.stream','Ponce_De_Leon')
        saveimages('https://streaming5.mdottraffic.com/snapshots?application=rtplive&snap=051701.stream','Ocean_Springs')
        saveimages('https://streaming5.mdottraffic.com/snapshots?application=rtplive&snap=051907.stream','US_90_Pascagoula_High_Rise_Bridge')
        saveimages('https://streaming5.mdottraffic.com/snapshots?application=rtplive&snap=051805.stream','lngalls_Shipyard')
        saveimages('https://streaming5.mdottraffic.com/snapshots?application=rtplive&snap=052507.stream','US_90_MS_57')
        time.sleep(600)
    
start()

    

