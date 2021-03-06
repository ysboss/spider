from bs4 import BeautifulSoup
import os, urllib.request
import re
import time
import js2py
#http://www.houstontranstar.org/snapshots/cctv/3210.jpg

cameras = [[]]
####
#    [name, monitor, roadway, location, lat, lng, dir, path, validimg, frameCount, framePauseMs] 
#cameras = [
#   ['10 EAST @ SAN JACINTO', '0', 'IH-10 East', 'SAN JACINTO', '29.76824', '-95.355711', 'None', '1002.jpg', 'True', '6', '300'],
#   ['IH-45 NORTH @ SH-242 N', '0', 'IH-45 North', 'SH-242 N', '30.21547', '-95.45686', 'None', '261.jpg', 'True', '1', '0'],
#    ................
# ]
####

def getCamerasLink(weburl):
    content = urllib.request.urlopen(weburl).read()
    soup = BeautifulSoup(content,"html.parser")
    obj = soup.find_all('a', text="Traffic Cameras")
    print (obj) 
    cam_link = obj[0].attrs['href']    
    
    getSnapshotsJS(cam_link)    

def getSnapshotsJS(weburl):
    content = urllib.request.urlopen(weburl).read() 
    soup = BeautifulSoup(content,"html.parser")
    objs = soup.find_all('script')
    ssJS = url+objs[5].attrs['src']
    print (ssJS)
    getCameras(ssJS)

def getCameras(jsfileurl):
    urllib.request.urlretrieve(jsfileurl,'cm.js')    
    f = open('cm.js','r')
    lines = f.readlines()[32:]
    for line in lines:
        if line.startswith('camera'):
            p = line.replace('\n','').replace("'",'*').split('*')
            camera = []
            for i in range(10):
                camera.append(p[2*i+1])
            cameras.append(camera) 
        else:
            pass  

def download(path,name):
    imageurl = "http://www.houstontranstar.org/snapshots/cctv/"+path
    data = urllib.request.urlopen(imageurl).read()
    imageNameTmp = name.replace(" ","_")+".jpg"
    imageName = imageNameTmp.replace("/","_")
    image = open(imageName,'wb')
    image.write(data)
    image.close()

    #j=s"\nconsole.dir(cctvCameras);"
    #js=js+"\nreturn (cctvCameras[0]);"
    #result = "my js:"+ int(js2py.eval_js(js))
    #print (js2py.eval_js(js))

#js2py.translate_file('cm.js','tran.py')




 #image_url = re.search("(?P<url>https?://[^\s]+stream)", link.get('onclick')).group("url")
         #saveimages(image_url, foldername) 

url = "https://traffic.houstontranstar.org"
getCamerasLink(url)


# print (cameras[1][7])
# download(cameras[4][7],cameras[4][0])
 
    
for i in range(1,len(cameras)):
    print (cameras[i][7])
    if (cameras[i][7]=="253.jpg" or cameras[i][7]=="417.jpg" or cameras[i][7]=="430.jpg" or cameras[i][7]=="1908.jpg" 
       or cameras[i][7]=="1909.jpg" or cameras[i][7]=="3211.jpg" or cameras[i][7]=="3223.jpg" or cameras[i][7]=="3204.jpg"
       or cameras[i][7]=="3206.jpg" or cameras[i][7]=="3207.jpg" or cameras[i][7]=="3107.jpg" or cameras[i][7]=="3227.jpg"):
        continue
    download(cameras[i][7],cameras[i][0])
    
    
    
    
    
    
    
    
    
