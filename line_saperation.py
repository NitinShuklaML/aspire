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


#print(len(sys.argv))
#print(str(sys.argv[1]))

frags=data["fragments"]
snippet_start=float(0.0)
prev_snippet_end=float(0.0)
sentence=str("")
complete_transcript=""
sentence_length=int(0)

for snippet in frags:
    if float(snippet["begin"])-float(prev_snippet_end)<= 1.0 and float(snippet["end"])-float(snippet["begin"]) <= 1.0:
        sentence= sentence + " " + snippet["lines"][0]
        sentence=sentence.replace("utterance-id1","").replace("[laughter]","").replace("[noise]","").strip() + "\n\n"            
        prev_snippet_end = snippet["end"]

        if sentence_length < 11:
            sentence_length += 1

        else:
            sentence_length%=10

    
    else:
        complete_transcript = complete_transcript + sentence + "\n"
        sentence = str("")
        sentence= sentence + " " + snippet["lines"][0]        
        sentence=sentence.replace("utterance-id1","").replace("[laughter]","").replace("[noise]","").strip() + "\n\n"
        prev_snippet_end = snippet["end"]

print(complete_transcript)

