#!/usr/bin/python

import sys
import json


with open('/home/nitin/audio/map.json') as json_file:
        data = json.load(json_file)

temp_trans=open("transient_transcript.txt","w+")#print(data)

def segmentation_transcript(data):
        try:
            frags=data["fragments"]
            snippet_start=float(0.0)
            snippet_end=float(0.0)
            sentence=""
            complete_transcript=""
        except:
            print("Your JSON data is malformed check if fragments setion is formed?")
            sys.exit(1)

        for snippet in frags:
            if float(snippet["end"])-float(snippet["begin"]) <= 1.0:
                sentence=sentence + " " +snippet["lines"][0]
                snippet_end=float(snippet["end"])

            else:
                sentence=sentence + " " + snippet["lines"][0]+ "\n"
                complete_transcript+="\n"+sentence                
                sentence=str("")
                snippet_end=float(snippet["end"])
        print(complete_transcript)
        temp_trans.write(complete_transcript)
        temp_trans.close()
                                                                                                                                                                                                    

try:
    input_arg_string = data
except:
    print("Your input dosen't seem to be a json file")
    sys.exit(1)

sample_dict = {}

if type(input_arg_string) == type(sample_dict):  
    segmentation_transcript(input_arg_string)

else:
    print("Your json file is not properly formed check map.json in root/audio")











