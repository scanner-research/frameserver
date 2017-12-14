import requests
import os

print('Sending frame server request...')
r = requests.get('http://localhost:7500/fetch', params={
    'path': os.getcwd() + '/example.mp4',
    'frame': 1300,
    'scale': 0.5
})

with open('example.jpg', 'wb') as f:
    f.write(r.content)
    print('Successfully generated example.jpg')
