from hwang import Decoder
from storehouse import StorageConfig, StorageBackend, RandomReadFile
from flask import Flask, request, send_file, Response
import cv2
import os
import io
import sys
import traceback

app = Flask(__name__)

FILESYSTEM = os.environ['FILESYSTEM']
if FILESYSTEM == 'google':
    config = StorageConfig.make_gcs_config(os.environ['BUCKET'])
else:
    config = StorageConfig.make_posix_config()
storage = StorageBackend.make_from_config(config)


@app.route("/fetch")
def fetch():
    try:
        path = request.args.get('path')
        frame = int(request.args.get('frame'))
        scale = request.args.get('scale', None)
        height = request.args.get('height', None)

        if FILESYSTEM == 'local':
            path = '/host' + path

        video_file = RandomReadFile(storage, path.encode('ascii'))

        video = Decoder(video_file)
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

    except Exception:
        return Response(traceback.format_exc(), mimetype='text/plain')


@app.route("/cache")
def cache():
    path = request.args.get('path')
    frame = [int(s) for s in request.args.get('frames').split(',')]
    # TODO
