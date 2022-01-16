import sqlite3, json

#(j, f[j]["name"], f[j]["level"], f[j]["last_action_relative"], f[j]["link"], i)

val = []

db = sqlite3.connect('orange_final.db')
# db.execute("CREATE TABLE data (id INT PRIMARY KEY, name VARCHAR(255), lvl INT, last_action VARCHAR(255),link VARCHAR(255), bstat INT)")


with open('datas.json','r') as file:
    f = json.load(file)

for i in f:
    val += [(int(i),f[i]["name"], f[i]["level"], f[i]["last_action_relative"],f[i]["link"], int(f[i]["bstats"]))]
db.executemany("INSERT INTO data VALUES (?,?,?,?,?,?)", val)

db.commit()
print('Sueces')