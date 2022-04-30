# import urllib.request
# import urllib
import requests

url = 'http://porno365.plus/movie/29005'

r = requests.get(url, stream = True)

with open('video.mp4', 'wb') as f:
    f.write(r.content)
# with open('vid.mp4', 'wb') as f:
#     for chunk in r.iter_content(chunk_size=1024*1024):
#         if chunk:
#             f.write(chunk)

# r = urllib.request.urlretrieve(url, 'out.mp4')
# with open('out.mp4', 'wb') as f:
    # f.write(r.read())
# try:
#     print('Starting download...\n')
#     urllib.request.urlretrieve(url, 'out.mp4')
#     print('Download completed')
# except Exception as e:
#     print(e)
