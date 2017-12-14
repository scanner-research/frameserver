# frameserver

This is a utility for efficiently serving randomly-accessed frames in a video.

## Setup
First, install [Docker](https://docs.docker.com/engine/installation/#supported-platforms), [Python 2.7](https://www.python.org/downloads/), and [pip](https://pip.pypa.io/en/stable/installing/).

```
$ git clone https://github.com/scanner-research/frameserver
$ cd frameserver
$ pip install docker-compose requests
$ docker-compose pull
$ docker-compose up -d
```

This spawns a server on port 7500 listening for frame requests.

## Usage

Here's an example of using the Python [requests](http://docs.python-requests.org/en/master/) library to get a frame. Look at the [example.py](https://github.com/scanner-research/frameserver/blob/master/example.py) script. We get frame 1300 at 1/2 scale from the video `example.mp4`.

To run this file, from inside the root of this repository, run:

```
$ pip install youtube-dl
$ youtube-dl "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -f mp4 -o example.mp4
$ python example.py
```

This generates a file `example.jpg` which you can scp/open.
