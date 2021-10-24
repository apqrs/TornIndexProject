import json

with open("data/under200m.json", 'r') as file:
    file = json.load(file)
dat={}
for id in file:
    link = f"https://www.torn.com/profiles.php?XID={id}"
    dat[id] = [file[id]["name"],file[id]["level"],file[id]["last_action_relative"]]

# print(dat.items())

i= sorted(dat.items(), key=lambda x:x[1][1], reverse = True)
print(i)