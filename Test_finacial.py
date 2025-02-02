from flask import Flask, render_template, request, redirect
import sqlite3
import json
import requests

database = "C:\\Users\\jackhsu\\Documents\\Unisoon\\規格\\程式_python_測試\\datafile.db"

app = Flask(__name__)
@app.route("/")                         # 首頁
def home():
    conn = sqlite3.connect("C:\\Users\\jackhsu\\Documents\\Unisoon\\規格\\程式_python_測試\\datafile.db")
    cursor = conn.cursor()
    cursor.execute(f"select * from cash")
    rows = cursor.fetchall()
    #for row in rows:
    #    print ("len:" + str(len(row)))
    #    p = ""
    #    for col in row:
    #        p += f"{col}, "
    #    print(p)
    conn.close()
    taiwan_dollar = 0
    us_dollar = 0
    total_dollar = 0
    for row in rows:
        taiwan_dollar += row[1]
        us_dollar += row[2]
    r=requests.get('https://tw.rter.info/capi.php')
    currency=r.json()
    total_dollar = taiwan_dollar + (us_dollar * currency["USDTWD"]["Exrate"])
    print("currency: " + str(currency["USDTWD"]["Exrate"]))
    print(f"taiwan dollar: {taiwan_dollar}")
    print(f"us dollar: {us_dollar}")
    print(f"total dollar: {total_dollar}")
    data = {}
    data["currency"] = currency["USDTWD"]["Exrate"]
    data["us"] = us_dollar
    data["td"] = taiwan_dollar
    data["total"] = total_dollar
    data["cash_result"] = rows
    return render_template("Index.html", data=data)

@app.route("/cash")                     # 現今庫存表單
def cash():
    return render_template("cash.html")

@app.route("/cash", methods=["POST"])   # 新增一筆現金紀錄(台幣, 美金, 備註, 日期)
def cash_post():
    try:
        #return f"thanks save: {request.values['taiwan_dollars'], request.values['us_dollars'], request.values['note'], request.values['savedate']}" 
        conn = sqlite3.connect("C:\\Users\\jackhsu\\Documents\\Unisoon\\規格\\程式_python_測試\\datafile.db")
        cursor = conn.cursor()
        cursor.execute(f"insert into cash(taiwanese_dollars, us_dollars, note, date_info) values({request.values['taiwan_dollars']}, {request.values['us_dollars']}, '{request.values['note']}', '{request.values['savedate']}')")
        #cursor.execute("insert into cash(taiwanese_dollars, us_dollars, note, date_info) values(200, 91.01, \"test str2\", \"2024/012/30\")")
        conn.commit()
        cursor.execute("select * from cash")
        rows = cursor.fetchall()
        c = 0
        for row in rows:
            c = c+1
            print(f"row{c}: {row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}")
        conn.close()
        return  redirect("/")
        
        
    except Exception as e:
        return "cash err: " + str(e)


@app.route("/stock")    # 股票庫存表單
def stock():
    return render_template("stock.html")


if(__name__== "__main__"):
    app.run(debug= True)
    