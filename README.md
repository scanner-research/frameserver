# frameserver

`frameserver` is a utility for efficiently serving randomly-accessed frames in a video.

## Setup
First, install [Docker](https://docs.docker.com/engine/installation/#supported-platforms), [Python 2.7](https://www.python.org/downloads/), and [pip](https://pip.pypa.io/en/stable/installing/).

```bash
$ git clone https://github.com/scanner-research/frameserver
$ cd frameserver
$ pip install docker-compose
$ docker-compose pull
$ docker-compose up -d
```

This spawns a server on port 7500 listening for frame requests.

## Example

Here's an example of using the Python [requests](http://docs.python-requests.org/en/master/) library to get a frame. Look at the [example.py](https://github.com/scanner-research/frameserver/blob/master/example.py) script. We get frame 1300 at 1/2 scale from the video `example.mp4`.

To run this file, from inside the root of this repository, run:

```bash
$ pip install youtube-dl requests
$ youtube-dl "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -f mp4 -o example.mp4
$ python example.py
```

This generates a file `example.jpg` which you can scp/open.

## Usage

The server exposes the GET endpoint `/fetch`. This takes the following arguments:
* `path` (required, string): absolute path (if local) or bucket-relative path (if cloud) to the video
* `frame` (required, integer): number of the frame in the video to retrieve
* `scale` (optional, float): relative size to change the image (2.0 is twice as big, 0.5 is half as big)
* `height` (optional, integer): target height to rescale the image to (keeps width proportional, i.e. maintains aspect ratio)

It returns a JPEG binary image if successful, and a plain text Python traceback on failure.
