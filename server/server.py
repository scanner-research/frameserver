from flask import Flask, Response
from scannerpy import Database, Job
import sys

app = Flask(__name__)
db = Database()

def _print(s):
    print s
    sys.stdout.flush()

@app.route('/', defaults={'path':''})
@app.route('/<path:path>')
def index(path):
    _print(path)
    N = 20
    frame = db.table('example').as_op().gather([N])
    resized = db.ops.Resize(frame=frame, width=640, preserve_aspect=True)
    compressed = db.ops.ImageEncoder(frame=resized)
    job = Job(columns=[compressed], name='_ignore')
    output = db.run(job, force=True, show_progress=False)
    _, jpg = next(output.load(['img']))
    return Response(jpg, mimetype='image/jpeg')
