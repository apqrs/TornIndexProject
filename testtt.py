import sqlite3, json

db = sqlite3.connect('orange.db')

k = list(db.execute("Select * from data where lvl>40;"))
# for y in k:
#     print(y)
print(k)

# # db.execute("CREATE TABLE data (id INT PRIMARY KEY, name VARCHAR(255), lvl INT, last_action VARCHAR(255),link VARCHAR(255))")
# val = []
# list = ['under2k','under25k','under250k','under2m','under20m']

# for i,name in enumerate(list):
#     n = f'data/{name}.json'
#     with open(n,'r') as file:
#         f = json.load(file)
#     for j in f:
#         value = (j, f[j]["name"], f[j]["level"], f[j]["last_action_relative"], f[j]["link"], i)
#         val += [value]
    

# db.executemany("INSERT INTO data VALUES (?,?,?,?,?,?)", val)

# db.commit()
# print('Success')