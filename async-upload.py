import time
import requests

from image_upload import ImageTweet
from video_upload import VideoTweet
from utilities import *

from auth import *

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/health')
def health():
    tweet()
    return '200 OK'

@app.route('/auth')
def auth():
    getGoogleAuth()
    return '200 OK'


def tweet():

    file = getRandomFile()
    print(file)

    if file['extension'] == 'mp4':
        videoTweet = VideoTweet(file['title'])
        videoTweet.tweet()

    if file['extension'] == 'png' or file['extension'] == 'jpg':
        imageTweet = ImageTweet()
        imageTweet.tweet(file['title'])
        os.remove(file['title'])

def ping():

    try:
        r = requests.head("https://csmsc.onrender.com")
        print(r.status_code)

    except requests.ConnectionError:
        print("failed to connect")

if __name__ == '__main__':
    app.run()
