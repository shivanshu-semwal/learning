import json

data = json.load(open("videos.json", "r+"))

videos = data["entries"]
challenges_videos = [video for video in videos if video["title"].startswith("Coding Challenge")]

json.dump(challenges_videos, open("challenges.json", "w+"))
