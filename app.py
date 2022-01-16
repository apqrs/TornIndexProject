from flask import Flask, render_template, url_for, flash, redirect, request
import json, sqlite3



app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/orangewait")
def orange():
    return render_template("wait.html")



@app.route("/show", methods = ["POST"])
def show():
    selector = request.form.get("range")

    dat = {}
    name = ""
    if selector == "2k":
        name = "under2k"
        sel = 0
    elif selector=="2k-25k":
        name = "under25k"
        sel = 1
    elif selector == "25k-250k":
        name = "under250k"
        sel = 2
    elif selector == "250k-2m":
        name = "under2m"
        sel = 3
    elif selector == "2m-25m":
        name = "under20m"
        sel = 4


    name = f"data/{name}.json"

    # with open(name,'r') as file:
    #     file = json.load(file)
    db = sqlite3.connect("orange.db")
    file = list(db.execute(f"SELECT * FROM data WHERE bstats={sel} order by lvl desc"))

    data = file

    name = name.replace('under','baldr')

    with open(name,'r') as file:
        file = json.load(file)

    bdata = file



    return render_template("index.html", data = data, bdata = bdata, nam = selector)

@app.route("/trade", methods=['GET','POST'])
def tradeCalc():
    if request.method == 'GET':
        return render_template("calc.html")
    else:
        items = request.form.get('tradeItems')
        import gspread, json, time, requests, math
        from oauth2client.service_account import ServiceAccountCredentials


        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("data/test.json", scope)

        client = gspread.authorize(creds)

        sheet = client.open("ZTrade Price List").sheet1


        it={'Sheep Plushie': (2, 2),
            'Teddy Bear Plushie': (3, 2),
            'Kitten Plushie': (4, 2),
            'Jaguar Plushie': (5, 2),
            'Wolverine Plushie': (6, 2),
            'Nessie Plushie': (7, 2),
            'Red Fox Plushie': (8, 2),
            'Monkey Plushie': (9, 2),
            'Chamois Plushie': (10, 2),
            'Panda Plushie': (11, 2),
            'Lion Plushie': (12, 2),
            'Camel Plushie': (13, 2),
            'Stingray Plushie': (14, 2),
            'Dahlia': (2, 5),
            'Crocus': (3, 5),
            'Orchid': (4, 5),
            'Heather': (5, 5),
            'Ceibo Flower': (6, 5),
            'Edelweiss': (7, 5),
            'Peony': (8, 5),
            'Cherry Blossom': (9, 5),
            'African Violet': (10, 5),
            'Tribulus Omanense': (11, 5),
            'Banana Orchid': (12, 5),
            'Bottle of Beer': (18, 2),
            'Erotic DVD': (21,2),
            'Can of Munster': (5,8),
            'Can of Red Cow': (6,8),
            'Can of Taurine Elite': (7,8),
            'Can of Santa Shooters': (8,8),
            'Can of Rockstar Rudolph': (9,8),
            'Can of X-MASS': (10,8),
            'Can of Goose Juice': (11,8),
            'Can of Damp Valley': (12,8),
            'Can of Crocozade': (13,8),}


        notFound = []
        money = 0
        order = ''
        for line in items.split('\n'):
            data = line.split('$')[0].split()
            num = int(data[-1][1:])
            name = ' '.join(data[:-1])
            if name in it:
                row,column = it[name]
                val = int(sheet.cell(row,column).value.replace(',',''))
                money += val * num

                strName = str(name).ljust(30,' ')

                strNum = '{:,}'.format(num)
                strNum = strNum.rjust(10,' ')

                strVal = '$' + '{:,}'.format(val)
                strVal = strVal.rjust(10,' ')

                NumxVal = f'{strNum} x {strVal}'
                NumxVal = NumxVal.rjust(25,' ')
                NumxVal = NumxVal

                strNumxVal = '{:,}'.format(num*val)
                strNumxVal = '$'+strNumxVal

                strNumxVal = strNumxVal.rjust(15,' ')

                line = f'{strName}{NumxVal}{strNumxVal}'


                order += line + '\n'




            else:
                notFound += [name]

        total ='$' + '{:,}'.format(money)
        mon = total[1:]
        order += '-' * 70 + '\n'
        total ='$' + '{:,}'.format(money)
        total = total.rjust(15,' ')
        endLine = 'Total |'.rjust(55,' ') + total
        order += endLine


        if  not order: order = 'None'
        data = {
        'api_dev_key': 'aoSBWC1-7oril_AieNcuETtizi77EqWG',
        'api_paste_code': order,
        'api_option': 'paste'
        }
        pastebin = requests.post('https://pastebin.com/api/api_post.php', data=data)
        pastebin = pastebin.text

        vals = [mon, pastebin, notFound]

        return render_template("calc.html", value = vals)



if __name__=="__main__":
    app.run(debug=False,host='0.0.0.0')


