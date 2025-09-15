import json
import hashlib

data = json.load(open("videos_list.json", "r+"))

for video in data:
    video["thumbnail"] = hashlib.md5(video["thumbnails"][-1]["url"].encode()).hexdigest()

json.dump(data, open("video_list_thumbnails.json", "w+"))
