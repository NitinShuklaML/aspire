#!/bin/bash

args=$1

brightcove/authentication.sh $args

./GenerateTranscript.sh $args.wav

cat ./line_saperation.py > saperated_text.txt

./AlignedTranscript.sh $args

./json2vtt.py

cat Sample.vtt
