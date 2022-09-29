from glob import escape
from flask import Flask, jsonify
import pandas as pd
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> hello world </h1>"

@app.route("/<name>")
def name(name):
    return f"<h1> welcome {escape(name)} to App </h1>"

@app.route("/annual-production/<int:api_well_number>")
def annual_production(api_well_number):
    data = pd.read_excel("data.xls")
    api_well_number_list = data["API WELL  NUMBER"]
    index = 1
    gas = 0
    brine = 0 
    oil = 0
    for i in api_well_number_list:
        index += 1
        if (i == api_well_number):
            oil += data[index-1:index]["OIL"].values[0]
            brine += data[index-1:index]["BRINE"].values[0]
            gas += data[index-1:index]["GAS"].values[0]
        print(type(gas))
    return jsonify({"annual_production_gas": int(gas),"annual_production_oil": int(oil),"annual_production_brine": int(brine)})


if __name__ == "__main__":
    app.run(debug=True,port=8080)