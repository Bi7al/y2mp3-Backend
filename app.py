from flask import Flask

app = Flask(__name__)


@app.route('/<URL>', methods=['POST'])
def convert_video(URL):
    return f"URL of the video is : {URL}"
@app.route('/', methods=['POST','GET'])
def convert_video():
    return "This is the Default Route for Youtube to Mp3 Site"













# Requirements for Future 
# flask-cors==4.0.0
# pytubefix==0.2.0
# ffmpeg-python==0.2.0
# nodejs