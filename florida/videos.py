import os, urllib.request
import m3u8, shutil, time
import ffmpy


# https://58f0f58ecd733.streamlock.net:444/pwillyspier/pwillyspiercam/chunklist_w922371290.m3u8

# https://58f0f58ecd733.streamlock.net:444/pwillyspier/pwillyspiercam/media_w922371290_59675.ts


def parseurl(main_url, m3u8, loc_name):
    
    tmpDir = 'tmp/' + loc_name
    if not os.path.exists(tmpDir):
        os.makedirs(tmpDir)
        
    m3u8Url = main_url + '/' + m3u8
    m3u8Path = tmpDir + '/' + m3u8
    try:
        
        # download m3u8 file 
        with urllib.request.urlopen(m3u8Url) as response, open(m3u8Path, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        
        # parse m3u8 file to get .ts file
        with open(m3u8Path, 'r') as playlist:
            ts_filenames = [line.rstrip() for line in playlist
                           if line.rstrip().endswith('.ts')]
        first_ts = ts_filenames[0]
    
        download(main_url, first_ts, loc_name, tmpDir)
    except Exception as ex_results:
        print ("Error: ", ex_results)
    
    pass 
    
    
def download(main_url, ts, loc_name, tmp_dir):
    
    videoDir = 'videos/' + loc_name
    if not os.path.exists(videoDir):
        os.makedirs(videoDir)
    
    tsUrl = main_url + '/' + ts
    tsPath = tmp_dir + '/' + ts
    
    # download .ts file
    with urllib.request.urlopen(tsUrl) as response, open(tmp_dir+'/'+ts, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    
    
    # convert .ts file to .mp4 file and save
    videoPath = videoDir + '/' + loc_name + '_' + time.strftime("%d-%m-%Y-%H-%M-%S") + '.mp4'
    
    cmd = 'ffmpeg -i ' + tsPath + ' ' + videoPath
    os.system(cmd)

def start():
    for gap in range(10000):
        
        # https://pwillys.com/beach-cam/
        parseurl('https://58f0f58ecd733.streamlock.net:444/pwillyspier/pwillyspiercam',
                 'chunklist_w922371290.m3u8','pineapple_willy_1')
        parseurl('https://58f0f58ecd733.streamlock.net:444/pwillys/pwillysbeachcam',
                 'chunklist_w1477564053.m3u8','pineapple_willy_2')
        
        
        #parseurl('https://58f0f58ecd733.streamlock.net:444/sharkyssunset/sharkyssunsetcam',
        #         'chunklist_w931049545.m3u8','sharky_beach_1')
        #parseurl('https://58f0f58ecd733.streamlock.net:444/sharkyssunset/sharkyssunsetcam',
        #         'chunklist_w601157767.m3u8','sharky_beach_2')
        
        # https://sharkysbeach.com/panama-city-beach-webcam-at-sharkys-beachfront-restaurant/
        parseurl('https://58f0f58ecd733.streamlock.net:444/sharkys/sharkysbeachcam', 
                 'chunklist_w1377948666.m3u8','sharky_beach_2' )
        
        # https://mexicobeach.com/mexico-beach/beach-cam/ 
        parseurl('https://b6.hdrelay.com/camera/8c37a607-6ab7-4cb5-a289-a46b96d2bf1a/relay',
                 'chunklist_w1797092158.m3u8','mexico_beach')
        
        # https://www.schooners.com/multimedia/beachcam.htm
        parseurl('https://58f0f58ecd733.streamlock.net:444/schoonersbeachHDCam830294711349/schbeach',
                 'chunklist_w1546822475.m3u8','schbeach')
        
        
        # http://gulfcrestcondominiums.com/hdcam/
        parseurl('https://e1-na5.angelcam.com/m7-na3/1172',
                 'playlist.m3u8?token=eyJhbGlhcyI6IjExNzIiLCJ0aW1lIjoxNTM5MTE4OTQzMDE1OTg4LCJ0aW1lb3V0IjozNjAwfQ%3D%3D.18e60dd714a5c2bde246f7e5d1c752eec9800ed552340cb5428c7f38b3e1de19','gulfCrest')
        
        
        # https://www.hipcbeach.com/holiday-inn-resort-beach-cam/
        parseurl('https://5a8473aac9c17.streamlock.net/live/roof.stream',
                 'chunklist_w619630066.m3u8','Holiday_Inn')
        
        
        # https://www.watersportspc.com/webcam
        parseurl('https://s19.ipcamlive.com/streams/135bba7a5874f1aee',
                 'stream.m3u8','Adventures_at_Sea')
        
        time.sleep(300)
        
start()





