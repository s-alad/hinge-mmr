import json
import os

# open matches.json
f = open('data/matches.json', 'r')
data = json.load(f)
f.close()

likes = 0
matches = 0


for m in data:
    if "like" in m: likes += 1
    if "match" in m: matches += 1


print("Likes: " + str(likes))
print("Matches: " + str(matches))
print("MMR: " + str(matches/likes*100) + "%")   