#!/bin/bash

args=$1

brightcove/authentication.sh $args
./GenerateTranscript.sh $args.wav
./AlignTranscript.sh $args

cat api/map.json



