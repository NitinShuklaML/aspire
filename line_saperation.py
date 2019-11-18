#!/usr/bin/env python

# Importing json Module for reading the incoming JSON files

import json
import sys


# Reading JSON file from current Directory

with open('map.json') as json_file:
        data = json.load(json_file)

transcript = json.dumps(data, indent=4)
#print(transcript)
#print(type(data))

sample_dict = {}
#print(type(sample_dict))
if type(data) == type(sample_dict):
    print("")

else:
    print("JSON seems to be malformed")


print(len(sys.argv))
#print(str(sys.argv[1]))

frags=data["fragments"]
snippet_start=float(0.0)
prev_snippet_end=float(0.0)
sentence=str("")
complete_transcript=""

for snippet in frags:
    if float(snippet["begin"])-float(prev_snippet_end)<= 1.0 and float(snippet["end"])-float(snippet["begin"]) <= 1.0:
        sentence= sentence + " " + snippet["lines"][0]
        sentence=sentence.replace("utterance-id1","").replace("[laughter]","").replace("[noise]","").strip()
        prev_snippet_end = snippet["end"]

       
    else:
        complete_transcript = complete_transcript + sentence + "\n"
        sentence = str("")
        sentence= sentence + " " + snippet["lines"][0]        
        sentence=sentence.replace("utterance-id1","").replace("[laughter]","").replace("[noise]","").strip()
        prev_snippet_end = snippet["end"]

print(complete_transcript)

