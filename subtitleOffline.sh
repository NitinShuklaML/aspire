#!/bin/bash

args=$1

./authentication.sh $args

echo $(./GenerateTranscript.sh $args.wav)

rm -rf $args.wav

echo ${args}_saperated_text.txt

./segment_transcripts.py ${args}_finalfinal.txt > ${args}_saperated_text.txt

rm -rf ${args}_finalfinal.txt

echo "" > ${args}_map.json

#cat ./line_saperation.py > saperated_text.txt

./AlignTranscript.sh $args

rm -rf $args.mp4 ${args}_saperated_text.txt

echo "" > $(pwd)/vtts/$args.vtt

./json2vtt.py $args

rm -rf ${args}_map.json

cat $(pwd)/vtts/$args.vtt
