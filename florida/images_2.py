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
        
        saveimages('http://tmc.baycountyfl.gov/CameraImages/Camera85.jpg?t=1539187457291','1')
        
        saveimages('http://tmc.baycountyfl.gov/CameraImages/90/snap_c1.jpg?t=1539187363599', '2')
        
        saveimages('http://tmc.baycountyfl.gov/CameraImages/53/snap_c1.jpg?t=1539187562731','3')
        
        saveimages('http://tmc.baycountyfl.gov/CameraImages/Camera54.jpg?t=1539187363599','4')      
        
        saveimages('http://tmc.baycountyfl.gov/CameraImages/Camera80.jpg?t=1539187586731','5')        
        
        saveimages('http://tmc.baycountyfl.gov/CameraImages/Camera73.jpg?t=1539187614160','6')
        
        saveimages('http://tmc.baycountyfl.gov/CameraImages/Camera74.jpg?t=1539187363599','7')
        
        saveimages('http://tmc.baycountyfl.gov/CameraImages/92/snap_c1.jpg?t=1539187363599','8')
        
        saveimages('http://tmc.baycountyfl.gov/CameraImages/01/snap_c1.jpg?t=1539187667337','9')
        
        saveimages('http://tmc.baycountyfl.gov/CameraImages/Camera86.jpg?t=1539187363599','10')
        
        saveimages('http://tmc.baycountyfl.gov/CameraImages/Camera10.jpg?t=1539187731321','11')
        
        saveimages('http://tmc.baycountyfl.gov/CameraImages/Camera52.jpg?t=1539187363599','12')
                 
        time.sleep(300)
                 
    

start()