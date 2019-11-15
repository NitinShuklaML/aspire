#!/usr/bin/env python

from flask import Flask
from flask import jsonify
from subprocess import Popen, PIPE
from subprocess import check_output
import run_setup



def get_subtitle_shell_script(args):
    stdout = check_output(['./subtitle.sh',str(args)]).decode('utf-8')
    return stdout

app = Flask(__name__) #app is the name of the object here

@app.route('/')
def home():
    return "<h1>Hello Kalyani...Bhaiyya Rocks!</h1>"

@app.route('/VideoDownload/<string:videoId>')
def Video(videoId):
    path="/home/nitin/audio"+videoId+".wav"
    #return "Under Cnstruction Bro "+videoId
    return jsonify(get_subtitle_shell_script(videoId))
    #return "<h1>Under Construction Bro" +videoId + "</h1>"


if __name__=="__main__":
    app.run(debug=True,port=8080)
