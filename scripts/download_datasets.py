import os
import gdown
import zipfile
from scripts import resize_youtube

LICENSE = """
These are either re-distribution of the original datasets or derivatives (through simple processing) of the original datasets. 
Please read and respect their licenses and terms before use. 
You should cite the original papers if you use any of the datasets.

For BL30K, see download_bl30k.py

Links:
DUTS: http://saliencydetection.net/duts
HRSOD: https://github.com/yi94code/HRSOD
FSS: https://github.com/HKUSTCV/FSS-1000
ECSSD: https://www.cse.cuhk.edu.hk/leojia/projects/hsaliency/dataset.html
BIG: https://github.com/hkchengrex/CascadePSP

YouTubeVOS: https://youtube-vos.org
DAVIS: https://davischallenge.org/
BL30K: https://github.com/hkchengrex/MiVOS
Long-Time Video: https://github.com/xmlyqing00/AFB-URR
"""

print(LICENSE)
print('Datasets will be downloaded and extracted to ./datasets/...')
reply = input('[y] to confirm, others to exit: ')
if reply != 'y':
    exit()

# Base directory for datasets
base_dir = os.path.join(os.getcwd(), '/bigtemp/rgq5aw/xmemDatasets')
os.makedirs(base_dir, exist_ok=True)

# """
# Static image data
# """
# static_dir = os.path.join(base_dir, 'static')
# os.makedirs(static_dir, exist_ok=True)
# print('Downloading static datasets...')
# gdown.download('https://drive.google.com/uc?id=1wUJq3HcLdN-z1t4CsUhjeZ9BVDb9YKLd', output=os.path.join(static_dir, 'static_data.zip'), quiet=False)
# print('Extracting static datasets...')
# with zipfile.ZipFile(os.path.join(static_dir, 'static_data.zip'), 'r') as zip_file:
#     zip_file.extractall(static_dir)
# print('Cleaning up static datasets...')
# os.remove(os.path.join(static_dir, 'static_data.zip'))

# """
# DAVIS dataset
# """
# davis_dir = os.path.join(base_dir, 'DAVIS')
# os.makedirs(davis_dir, exist_ok=True)
# os.makedirs(os.path.join(davis_dir, '2017'), exist_ok=True)

# print('Downloading DAVIS 2016...')
# gdown.download('https://drive.google.com/uc?id=198aRlh5CpAoFz0hfRgYbiNenn_K8DxWD', output=os.path.join(davis_dir, 'DAVIS-data.zip'), quiet=False)

# print('Downloading DAVIS 2017 trainval...')
# gdown.download('https://drive.google.com/uc?id=1kiaxrX_4GuW6NmiVuKGSGVoKGWjOdp6d', output=os.path.join(davis_dir, '2017', 'DAVIS-2017-trainval-480p.zip'), quiet=False)

# print('Downloading DAVIS 2017 testdev...')
# gdown.download('https://drive.google.com/uc?id=1fmkxU2v9cQwyb62Tj1xFDdh2p4kDsUzD', output=os.path.join(davis_dir, '2017', 'DAVIS-2017-test-dev-480p.zip'), quiet=False)

# print('Downloading DAVIS 2017 scribbles...')
# gdown.download('https://drive.google.com/uc?id=1JzIQSu36h7dVM8q0VoE4oZJwBXvrZlkl', output=os.path.join(davis_dir, '2017', 'DAVIS-2017-scribbles-trainval.zip'), quiet=False)

# print('Extracting DAVIS datasets...')
# with zipfile.ZipFile(os.path.join(davis_dir, 'DAVIS-data.zip'), 'r') as zip_file:
#     zip_file.extractall(davis_dir)
# os.rename(os.path.join(davis_dir, 'DAVIS'), os.path.join(davis_dir, '2016'))

# with zipfile.ZipFile(os.path.join(davis_dir, '2017', 'DAVIS-2017-trainval-480p.zip'), 'r') as zip_file:
#     zip_file.extractall(os.path.join(davis_dir, '2017'))
# with zipfile.ZipFile(os.path.join(davis_dir, '2017', 'DAVIS-2017-scribbles-trainval.zip'), 'r') as zip_file:
#     zip_file.extractall(os.path.join(davis_dir, '2017'))
# os.rename(os.path.join(davis_dir, '2017', 'DAVIS'), os.path.join(davis_dir, '2017', 'trainval'))

# with zipfile.ZipFile(os.path.join(davis_dir, '2017', 'DAVIS-2017-test-dev-480p.zip'), 'r') as zip_file:
#     zip_file.extractall(os.path.join(davis_dir, '2017'))
# os.rename(os.path.join(davis_dir, '2017', 'DAVIS'), os.path.join(davis_dir, '2017', 'test-dev'))

# print('Cleaning up DAVIS datasets...')
# os.remove(os.path.join(davis_dir, '2017', 'DAVIS-2017-trainval-480p.zip'))
# os.remove(os.path.join(davis_dir, '2017', 'DAVIS-2017-test-dev-480p.zip'))
# os.remove(os.path.join(davis_dir, '2017', 'DAVIS-2017-scribbles-trainval.zip'))
# os.remove(os.path.join(davis_dir, 'DAVIS-data.zip'))

# """
# YouTubeVOS dataset
# """
youtube_dir = os.path.join(base_dir, 'YouTube')
os.makedirs(youtube_dir, exist_ok=True)
os.makedirs(os.path.join(youtube_dir, 'all_frames'), exist_ok=True)

print('Downloading YouTubeVOS train...')
gdown.download('https://drive.google.com/uc?id=13Eqw0gVK-AO5B-cqvJ203mZ2vzWck9s4', output=os.path.join(youtube_dir, 'train.zip'), quiet=False)
print('Downloading YouTubeVOS val...')
gdown.download('https://drive.google.com/uc?id=1o586Wjya-f2ohxYf9C1RlRH-gkrzGS8t', output=os.path.join(youtube_dir, 'valid.zip'), quiet=False)
print('Downloading YouTubeVOS all frames valid...')
gdown.download('https://drive.google.com/uc?id=1rWQzZcMskgpEQOZdJPJ7eTmLCBEIIpEN', output=os.path.join(youtube_dir, 'all_frames', 'valid.zip'), quiet=False)

print('Extracting YouTube datasets...')
with zipfile.ZipFile(os.path.join(youtube_dir, 'train.zip'), 'r') as zip_file:
    zip_file.extractall(youtube_dir)
with zipfile.ZipFile(os.path.join(youtube_dir, 'valid.zip'), 'r') as zip_file:
    zip_file.extractall(youtube_dir)
with zipfile.ZipFile(os.path.join(youtube_dir, 'all_frames', 'valid.zip'), 'r') as zip_file:
    zip_file.extractall(os.path.join(youtube_dir, 'all_frames'))

print('Cleaning up YouTubeVOS datasets...')
os.remove(os.path.join(youtube_dir, 'train.zip'))
os.remove(os.path.join(youtube_dir, 'valid.zip'))
os.remove(os.path.join(youtube_dir, 'all_frames', 'valid.zip'))

print('Resizing YouTubeVOS to 480p...')
resize_youtube.resize_all(os.path.join(youtube_dir, 'train'), os.path.join(youtube_dir, 'train_480p'))

"""
YouTubeVOS2018 dataset
"""
youtube2018_dir = os.path.join(base_dir, 'YouTube2018')
os.makedirs(youtube2018_dir, exist_ok=True)
os.makedirs(os.path.join(youtube2018_dir, 'all_frames'), exist_ok=True)

print('Downloading YouTubeVOS2018 val...')
gdown.download('https://drive.google.com/uc?id=1-QrceIl5sUNTKz7Iq0UsWC6NLZq7girr', output=os.path.join(youtube2018_dir, 'valid.zip'), quiet=False)
print('Downloading YouTubeVOS2018 all frames valid...')
gdown.download('https://drive.google.com/uc?id=1yVoHM6zgdcL348cFpolFcEl4IC1gorbV', output=os.path.join(youtube2018_dir, 'all_frames', 'valid.zip'), quiet=False)

print('Extracting YouTube2018 datasets...')
with zipfile.ZipFile(os.path.join(youtube2018_dir, 'valid.zip'), 'r') as zip_file:
    zip_file.extractall(youtube2018_dir)
with zipfile.ZipFile(os.path.join(youtube2018_dir, 'all_frames', 'valid.zip'), 'r') as zip_file:
    zip_file.extractall(os.path.join(youtube2018_dir, 'all_frames'))

print('Cleaning up YouTubeVOS2018 datasets...')
os.remove(os.path.join(youtube2018_dir, 'valid.zip'))
os.remove(os.path.join(youtube2018_dir, 'all_frames', 'valid.zip'))

"""
Long-Time Video dataset
"""
long_video_dir = os.path.join(base_dir, 'long_video_set')
os.makedirs(long_video_dir, exist_ok=True)

print('Downloading long video dataset...')
gdown.download('https://drive.google.com/uc?id=100MxAuV0_UL20ca5c-5CNpqQ5QYPDSoz', output=os.path.join(long_video_dir, 'LongTimeVideo.zip'), quiet=False)
print('Extracting long video dataset...')
with zipfile.ZipFile(os.path.join(long_video_dir, 'LongTimeVideo.zip'), 'r') as zip_file:
    zip_file.extractall(long_video_dir)
print('Cleaning up long video dataset...')
os.remove(os.path.join(long_video_dir, 'LongTimeVideo.zip'))

print('Done.')
