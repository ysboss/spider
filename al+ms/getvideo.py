##  This script is for crawling vedio from www.mdottraffic.com in Mississippi  
## 

## import necessary libraries
import m3u8, shutil, time
import ffmpy, os
import urllib.request
  
url = 'https://streaming5.mdottraffic.com/rtplive/051807.stream/chunklist_w713564988.m3u8'
## input startdatetime and enddatetime using format like: ’Thu Oct 19 21:56:36 2017‘
## for example: start('Fri Oct 20 10:55:00 2017','Fri Oct 21 10:55:00 2017','10')
starttime = 'startdatetime'
endtime = 'enddatetime'

while (time.strftime("%c") < starttime):
        time.sleep(1)

## get substring information
chunklist = url[-25:]
firstUrl = url[0:57]
media = url[-15:-5]

## parse .m3u8 file to get .ts files
m3u8Path = 'tmp/'+chunklist
with urllib.request.urlopen(url) as response, open(m3u8Path, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
        
with open(m3u8Path, 'r') as playlist:
    ts_filenames = [line.rstrip() for line in playlist 
                   if line.rstrip().endswith('.ts')]
string = ts_filenames[0]
startNum = int(string[-8:-3])

## judge if file is exist
def ifFileExist(path):
    while(not os.path.exists(path)):
        downloadfile()
        time.sleep(3)

## download .ts files
def downloadfile():
    with urllib.request.urlopen(url) as response, open(m3u8Path, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
        
    with open(m3u8Path, 'r') as playlist:
        ts_filenames = [line.rstrip() for line in playlist 
                    if line.rstrip().endswith('.ts')]
  
    for i in range(3):
        ts = ts_filenames[i]
        tsurl = firstUrl+ts
        tsPath = 'tmp/'+ts
        while (not os.path.exists(tsPath)):
            with urllib.request.urlopen(tsurl) as response, open(tsPath, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
        #ifFileExist(tsPath)    

while (time.strftime("%c") < endtime):
    
    downloadfile()
    
    ## merge multi .ts files to one .ts file
    videoPath = 'tmp/'+str(startNum)+ '.ts'
    with open(videoPath, 'wb') as merged:
        for j in range(6):
            ts_path = 'tmp/media_'+media+'_'+str(startNum)+'.ts'
            print (ts_path)
            ifFileExist(ts_path)
            with open(ts_path, 'rb') as mergefile:
                shutil.copyfileobj(mergefile, merged)
            startNum+=1
            
    ## convert .ts file to .mp4 file and save
    infile = videoPath
    outfile = 'tmp/'+str(startNum-6)+'.mp4'
    cmd = 'ffmpeg -i '+videoPath+ ' '+ outfile
    print (cmd)
    os.system(cmd)
    print ('***************')
    
