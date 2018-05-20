from bs4 import BeautifulSoup
import os, urllib.request
import time


def saveimages(url,location):
    data = urllib.request.urlopen(url).read()
    fileName = location + '-'+time.strftime("%c")+'.jpg'
    path = '/home/syuan/reptiles/imgs_Alab/'+location
    filePath = os.path.join(path, fileName)
    image = open(filePath,'wb')
    image.write(data)
    image.close()
# revise test
def start():
    for gap in range(144):
        saveimages('http://mobalgortmc.dot.state.al.us:8090/snapshots/MOB-CAM-C055.jpg','I10E-MM30.4')
        saveimages('http://mobalgortmc.dot.state.al.us:8090/snapshots/MOB-CAM-C052.jpg','I10E-MM32.2')
        saveimages('http://mobalgortmc.dot.state.al.us:8090/snapshots/MOB-CAM-C056.jpg','I10E-MM29.8')
        saveimages('http://mobalgortmc.dot.state.al.us:8090/snapshots/MOB-CAM-C047.jpg','I10E@U90-98')
        saveimages('http://mobalgortmc.dot.state.al.us:8090/snapshots/MOB-CAM-C024.jpg','I10E@Water-St-west-vent')
        saveimages('http://mobalgortmc.dot.state.al.us:8090/snapshots/MOB-CAM-C073.jpg','I10E@Water-St')
        saveimages('http://mobalgortmc.dot.state.al.us:8090/snapshots/MOB-CAM-C060.jpg','I10W-MM27.6')
        saveimages('http://mobalgortmc.dot.state.al.us:8090/snapshots/MOB-CAM-C044.jpg','I10W-MM35.0')
        saveimages('http://mobalgortmc.dot.state.al.us:8090/snapshots/MOB-CAM-C010.jpg','US90-98-Bankhead-Entrance')
        saveimages('http://mobalgortmc.dot.state.al.us:8090/snapshots/MOB-CAM-C019.jpg','US90-98E-US31')
        saveimages('http://mobalgortmc.dot.state.al.us:8090/snapshots/MOB-CAM-C015.jpg','US90-98W-I10')
        saveimages('http://mobalgortmc.dot.state.al.us:8090/snapshots/MOB-CAM-C018.jpg','US90-98W-MM40')
        time.sleep(600)
    



    
start()