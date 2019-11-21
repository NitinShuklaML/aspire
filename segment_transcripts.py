#!/usr/bin/env python

import sys

args=str(sys.argv[1])

#print(args)

file1 = open(args,"r+")
some_data=file1.read()
file1.close()

#print(some_data)

some_data=some_data.replace("[noise]","").replace("[laughter]","").replace("utterance-id1","").strip()
complete_transcript=str("")

list_some_data=some_data.split()
some_data_len=len(list_some_data)
joint_string=[' '.join(list_some_data)] 
#print(joint_string)

for a in range(0,some_data_len,13):
    joint_string=[' '.join(list_some_data[a-13:a])] 
    complete_transcript=complete_transcript + "\n" + str(joint_string).replace("utterance-id1 ","").replace('[','').replace(']','').replace('\'','').replace('\"','') + "\n"
 
rem=len(list_some_data)%13
#print(len(list_some_data))
#print(rem)

if rem != 0:
    complete_transcript=complete_transcript+' '.join(list_some_data[-rem:])+"\n"
    

print(complete_transcript)
