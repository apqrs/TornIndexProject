from flask import Flask, render_template, url_for, flash, redirect, request
import json



app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/show", methods = ["POST"])
def show():
    selector = request.form.get("range")
    
    dat = {}
    name = ""
    if selector == "2k":
        name = "under2k"
    elif selector=="2k-25k":
        name = "under25k"
    elif selector == "25k-250k":
        name = "under250k"
    elif selector == "250k-2m":
        name = "under2m"
    elif selector == "2m-200m":
        name = "under200m"

    name = f"data/{name}.json"

    with open(name,'r') as file:
        file = json.load(file)
    
    for id in file:
        link = f"https://www.torn.com/profiles.php?XID={id}"
        dat[id] = [file[id]["name"],file[id]["level"],file[id]["last_action_relative"],link]

    dat = sorted(dat.items(), key=lambda x:x[1][1], reverse = True)

    name = name.replace('under','baldr')

    with open(name,'r') as file:
        file = json.load(file)
    bdata = file
    


    return render_template("index.html", data = dat, bdata = bdata, nam = selector)

if __name__=="__main__":
    app.run(debug=False,host='0.0.0.0')


