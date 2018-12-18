from bs4 import BeautifulSoup
#import os, urllib.request
import os, urllib, requests
import time
import pathlib

##  charlotte, NC

def saveimages(url,location):
    #data = urllib.request.urlopen(url).read()
    data = requests.get(url).content
    fileName = location + '-'+time.strftime("%c")+'.jpg'
    path = '/home/syuan/reptiles/north_carolina/images5/'+location
    pathlib.Path(path).mkdir(parents=True, exist_ok=True) 
    filePath = os.path.join(path, fileName)
    image = open(filePath,'wb')
    image.write(data)
    image.close()
# revise test
def start():
    for gap in range(100000):
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=0I0077N0001-43_IMG.JPG','I-77_Rest_Area')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=0I0077s0002-02_img.jpg','I-77_I-485_South')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=0I0077N0003-58_IMG.JPG','I-77_Nations_Ford_Rd')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=0I0077n0004-87_img.jpg','I-77_Tyvola_Rd')         
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=0I0077S0006-27_IMG.JPG','I-77_South_Tryon_Street')        
        
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=0I0077s0006-79_img.jpg','I-77_S_of_Clanton_Rd')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=0I0077S0009-25_IMG.JPG','I-77_Wilkinson_Blvd')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=0I0077N0010-30_IMG.JPG','I-77_Trade_Street')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=0I0077N0011-02_IMG.JPG','I-77_South_of_Brookshire_Frwy')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=nc0016n0005-24_img.jpg','NC-16_Beatties_Ford_Rd')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=0I0085S0039-10_IMG.JPG','I-85_Statesville_Ave')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=0I0085S0040-30_IMG.JPG','I-85_Graham_Street')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=0I0085S0041-30_IMG.JPG','I-85_Sugar_Creek_Rd')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=0I0085S0042-21_IMG.JPG','I-85_South_of_US-29')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=0I0085S0044-52_IMG.jpg','I-85_Harris_Blvd')
        saveimages('https://tims.ncdot.gov/TIMS/Cameras/viewimage.ashx?id=US002900000097_IMG.JPG','US_29_At_I-485')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=0I0085S0049-25_IMG.JPG','I-85_Concord_Mills_Blvd')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=0I0085N0049-30_IMG.JPG','I-85_B_Smith_Blvd')
        
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=0I0485I0016-63_IMG.JPG','I-485_South_of_Oakdale_Rd')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=0I0077n0018-47_img.jpg','I-77_N_of_Harris_Blvd')
    
                 
        time.sleep(600)
                 
    

start()