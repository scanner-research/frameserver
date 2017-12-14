from hwang import Decoder
from storehouse import StorageConfig, StorageBackend, RandomReadFile
from flask import Flask, request, send_file
import cv2
import os
import io

app = Flask(__name__)

config = StorageConfig.make_gcs_config(os.environ['BUCKET'])
storage = StorageBackend.make_from_config(config)

@app.route("/fetch")
def fetch():
    path = request.args.get('path')
    frame = int(request.args.get('frame'))
    scale = request.args.get('scale', None)
    height = request.args.get('height', None)

    video_file = RandomReadFile(storage, path.encode('ascii'))

    video = Decoder(video_file, size=video_file._size)  # TODO: make _size public function
    img = video.retrieve([frame])[0]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    [cur_height, cur_width, _] = img.shape
    target_width = None
    target_height = None
    if scale is not None:
        scale = float(scale)
        target_width = cur_width * scale
        target_height = cur_height * scale
    elif height is not None:
        height = float(height)
        target_height = height
        target_width = target_height / cur_height * cur_width

    if target_width is not None:
        img = cv2.resize(img, (int(target_width), int(target_height)))

    return send_file(io.BytesIO(cv2.imencode('.jpg', img)[1]), mimetype='image/jpg')

@app.route("/cache")
def cache():
    path = request.args.get('path')
    frame = [int(s) for s in request.args.get('frames').split(',')]
    # TODO
