#!/usr/bin/env python

from flask import Flask
from flask import jsonify
import run_setup

app = Flask(__name__) #app is the name of the object here

@app.route('/')
def home():
    return "<h1>Hello Kalyani...Bhaiyya Rocks!</h1>"

@app.route('/VideoDownload/<string:videoId>')
def Video(videoId):
    path="/home/nitin/audio"+videoId+".wav"
    return jsonify(run_setup.setup(videoId))
    #return "<h1>Under Construction Bro" +videoId + "</h1>"


if __name__=="__main__":
    app.run(debug=True,port=8080)
