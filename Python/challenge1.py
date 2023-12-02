from sdk import exodusSdk
from pathlib import Path
import time
from datetime import datetime
import json
import os
from dotenv import load_dotenv

load_dotenv()


BASE_URL = os.environ['BASE_URL']
print(BASE_URL)
USER = os.environ['API_USER']
print(USER)
API_KEY = os.environ['API_KEY']
print(API_KEY)
AWS_S3_ACCESS_KEY = os.environ['AWS_S3_ACCESS_KEY']
print(AWS_S3_ACCESS_KEY)
AWS_S3_SECRET_KEY = os.environ['AWS_S3_SECRET_KEY']
print(AWS_S3_SECRET_KEY)
AWS_S3_BUCKET = os.environ['AWS_S3_BUCKET']
print(AWS_S3_BUCKET )

lon = '-79.6'
lat = '43.7'
net = '2023-03-01 00:00:00'
nlt = '2023-03-04 00:00:00'
missionType = 'Hyperspectral'
missionDescription = 'WebNOVA Challenge 1'

satApi = exodusSdk(BASE_URL, USER, API_KEY)

# get available satellites
satellites = satApi.get_satellites()
print(f"{len(satellites)} stallites available")
for sat in satellites:
    print(f"-------------------------")
    print(sat)
    print(f"-------------------------")
# get satellite norad_id
noradId = satellites[0].norad_id

# get available instruments for the satellite with norad_id
instruments = satApi.get_instruments(noradId)
# we are using imager, instrument.id = 1
instrumentId = instruments[0].id

# get times on target
timesOnTarget = satApi.get_times_on_target(noradId, instrumentId, lon, lat, net, nlt)
print(f"-----------times----------")
for t_on_target in timesOnTarget:
    print(t_on_target)
print(f"-------------------------")
# create a mission, schedule data retrieval according to the date_available value
mission = satApi.create_mission(
    noradId,
    instrumentId,
    lon, 
    lat, 
    net, 
    nlt, 
    missionDescription, 
    missionType
)
# the response from the above return data key and date when the data is available
dateAvailable = mission.date_available
satDataKey = mission.data_key

# get the data information
satDataInfo = satApi.get_download(satDataKey)

# download an archive with the mission data
dataUrl = satDataInfo.data_url

# sleep 2 seconds, wait for file to be generated on S3
time.sleep(2)
#download zip file
p = Path(dataUrl)
now = datetime.now()
satApi.download_file('downlink/'+p.name, AWS_S3_ACCESS_KEY, AWS_S3_SECRET_KEY, AWS_S3_BUCKET, 'FILE_NAME_'+now.strftime("%m-%d-%Y-%H-%M-%S") +'.zip')
