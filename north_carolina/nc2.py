from bs4 import BeautifulSoup
#import os, urllib.request
import os, urllib, requests
import time
import pathlib

    

def saveimages(url,location):
    #data = urllib.request.urlopen(url).read()
    data = requests.get(url).content
    fileName = location + '-'+time.strftime("%c")+'.jpg'
    path = '/home/syuan/reptiles/north_carolina/images2/'+location
    pathlib.Path(path).mkdir(parents=True, exist_ok=True) 
    filePath = os.path.join(path, fileName)
    image = open(filePath,'wb')
    image.write(data)
    image.close()
# revise test
def start():
    for gap in range(100000):
        saveimages('https://tims.ncdot.gov/TIMS/Cameras/viewimage.ashx?id=Hatteras_Inlet_South_Dock.jpg','MM_73')
        saveimages('https://tims.ncdot.gov/TIMS/Cameras/viewimage.ashx?id=NC12_Mirlo_Beach.jpg','MM_38')
        saveimages('https://tims.ncdot.gov/TIMS/Cameras/viewimage.ashx?id=NC12_Temp_Bridge_over_New_Inlet.jpg','MM_32.5')
        saveimages('https://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=BonnerBridgeNorth.jpg','MM_25')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=us158-pasquotankriver.jpg','Elizabeth_City_Drawbridge')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=US158_Mall_Dr.jpg','MM_14')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=US158_Jockeys_Ridge.jpg','MM_12.5')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=US158_E_Barnes_St.jpg','MM_10.5')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=US158_W_Ocean_Bay_Blvd.jpg','MM_8')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=US158_3rd_St.jpg','MM_6.5')
        saveimages('https://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=US158_Helga_St.jpg','MM_5.5')
        saveimages('https://tims.ncdot.gov/TIMS/Cameras/viewimage.ashx?id=US158_Kitty_Hawk_Rd.jpg','MM_4')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=NC12_US158.jpg','MM_1.5')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=NC12_Sea_Oats_Tr.jpg','NC12_Sea_Oats_Tr')
        saveimages('https://tims.ncdot.gov/TIMS/Cameras/viewimage.ashx?id=NC12_Hillcrest_Dr.jpg','NC12_Hillcrest_Dr')
        saveimages('http://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=nc12-albacore.jpg','NC12-albacore')
        saveimages('https://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=us64-alligatorbr.jpg','us64-alligatorbr')
        saveimages('https://tims.ncdot.gov/tims/cameras/viewimage.ashx?id=US64_mm552.jpg','MM_552')
        
        time.sleep(600)
    

start()