import json

with open("data/baldrlist.txt", 'r') as file:
    data = file.readlines()

under2k = {}
under25k = {}
under250k = {}
under2m ={}
under25m = {}
under200m = {}
for i in data:
    name, id, lvl, total, str, defe, spd, dxt = i.split()
    total = int(total)
    if total<=2000:
        under2k[id] = [name, lvl, str, defe, spd, dxt, total, f"https://www.torn.com/profiles.php?XID={id}"]
    elif total<=25000:
        under25k[id] = [name, lvl, str, defe, spd, dxt, total, f"https://www.torn.com/profiles.php?XID={id}"]
    elif total<=250000:
        under250k[id] = [name, lvl, str, defe, spd, dxt, total, f"https://www.torn.com/profiles.php?XID={id}"]
    elif total <= 2000000:
        under2m[id] = [name, lvl, str, defe, spd, dxt, total, f"https://www.torn.com/profiles.php?XID={id}"]
    elif total <= 25000000:
        under25m[id] = [name, lvl, str, defe, spd, dxt, total, f"https://www.torn.com/profiles.php?XID={id}"]
    elif total <= 200000000:
        under200m[id] = [name, lvl, str, defe, spd, dxt, total, f"https://www.torn.com/profiles.php?XID={id}"]

under2ka = sorted(under2k.items(), key = lambda x: x[1][6], reverse=True)
under25ka = sorted(under25k.items(), key = lambda x: x[1][6], reverse=True)
under250ka = sorted(under250k.items(), key = lambda x: x[1][6], reverse=True)
under2ma= sorted(under2m.items(), key = lambda x: x[1][6], reverse=True)
under25ma = sorted(under25m.items(), key = lambda x: x[1][6], reverse=True)
under200ma = sorted(under200m.items(), key = lambda x: x[1][6], reverse=True)

under2k = {}
under25k = {}
under250k = {}
under2m ={}
under25m = {}
under200m = {}

for f in under2ka:
    under2k[f[0]]= f[1]
for f in under25ka:
    under25k[f[0]]= f[1]
for f in under250ka:
    under250k[f[0]]= f[1]
for f in under2ma:
    under2m[f[0]]= f[1]
for f in under25ma:
    under25m[f[0]]= f[1]
for f in under200ma:
    under200m[f[0]]= f[1]


with open('data/baldr2k.json','w') as file:
    json.dump(under2k, file, indent=2) 

with open('data/baldr25k.json','w') as file:
    json.dump(under25k, file, indent=2) 

with open('data/baldr250k.json','w') as file:
    json.dump(under250k, file, indent=2) 

with open('data/baldr2m.json','w') as file:
    json.dump(under2m, file, indent=2) 

with open('data/baldr25m.json','w') as file:
    json.dump(under25m, file, indent=2) 

with open('data/baldr200m.json','w') as file:
    json.dump(under25m, file, indent=2) 

