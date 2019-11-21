#!/bin/bash

CLIENT_ID="1e199323-0fbf-41c2-931e-c36b2c38b582"
CLIENT_SECRET="SrG0yJ_VxQZJRqWzXIdC52Xg6f-k2W6SV4CYE3mkJql7WEzlRoPCXQbrvvejw2sdpzv1snn7auWzDGKxmH2zQg"
ACCOUNT_ID="2103045685001"
VIDEO_ID=$1

echo "client_id : "$CLIENT_ID
echo "client_secret :"$CLIENT_SECRET
echo "arguments : "$1
echo "Video id :"$VIDEO_ID

TOKEN=$(curl -s --data "grant_type=client_credentials" https://oauth.brightcove.com/v3/access_token --header "Content-Type: application/x-www-form-urlencoded" --user "$CLIENT_ID:$CLIENT_SECRET" | sed -E 's/.*access_token\"\:\"([^\"]+)\".*/\1/');

echo Your token $TOKEN

VIDEO_URL="https://cms.api.brightcove.com/v1/accounts/"$ACCOUNT_ID"/videos/"$VIDEO_ID"/sources"

echo "REQUEST_URL is : "$VIDEO_URL

REQUEST=$(curl -X GET -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" $VIDEO_URL)

echo $REQUEST > ${1::-4}.json

echo $(extract_json.py ${1::-4}.json)

wget -O $1.mp4 $extract_json.py ${1::-4}.json

ffmpeg -i $1.mp4 -acodec pcm_s16le -ar 8000 -ac 1 $1.wav

rm -rf ${1::-4}.json 


