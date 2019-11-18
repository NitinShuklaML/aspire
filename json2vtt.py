#!/usr/bin/env python


# Importing json Module for reading the incoming JSON files

import json

# Reading JSON file from current Directory

with open('map.json') as json_file:
    data = json.load(json_file)
    
transcript = json.dumps(data, indent=4)



# Initializing Empty List
# Initializimg an empty string for Transcripts

empty=['']
output="WEBVTT\n\n"

f=open("Sample.vtt","w+")

def convert_time(time,pos):    
    time = float(frags[pos])    
    time = time % (24 * 3600)
    hour = time // 3600    
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
    time %= 10
    millisec = int(time*1000)    
    if pos=="begin":
        return ("%02d:%02d:%02d.%03d --> " % (hour, minutes, seconds, millisec))          
    else:
        return (" %02d:%02d:%02d.%03d align:middle line:90%%" % (hour, minutes, seconds, millisec) + "\n")          


#f=open("Sample.vtt","a+")
#f.write("WEBVTT\n\n")

#f.write("WEBVTT\n\n")

for frags in data["fragments"]:      
    if float(frags["end"])-float(frags["begin"]) > 0 and frags["lines"] != empty:
        #print(float(frags["end"])-float(frags["begin"]))    
        #line=str(frags["lines"])[2:][:-2]+ "\n"
        #print(output)
        output = output + convert_time(float(frags["begin"]),"begin")
        output = output + convert_time(float(frags["end"]),"end") 
        output = output + str(frags["lines"])[2:][:-2] + "\n"
        output = output.replace("\"","")
        output = output.replace("\'","")
        #output=output + str(frags["lines"])[2:][:-2] + "\n"
        #f.write(frags["lines"][2:][:-2])
        #f.write("\n")
print(output)

f.write(output)
f.close()
