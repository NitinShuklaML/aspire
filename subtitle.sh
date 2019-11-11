#!/bin/bash

args=$1

../brightcove/authentication.sh $args
../GenerateTranscript.sh $args



