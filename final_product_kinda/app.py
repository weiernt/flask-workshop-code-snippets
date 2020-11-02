from flask import Flask, render_template, request
import requests
from wtforms import Form, TextField

app = Flask(__name__)
gh_link = "https://github.com/weiernt"

@app.route("/")
@app.route("/home")
def hello():
    return render_template("home_page.html", link=gh_link)

@app.route("/search")
def search():
    dictionary = get_request("AUS")
    list_of_data = dictionary["data"]

    return render_template("search_page.html", list_of_data=list_of_data)


def get_request(iso):
    url = "https://covid-api.com/api/reports"
    url = url + "?iso=" + iso 
    r = requests.request("GET", url)
    return r.json()

if __name__=="__main__":
    app.run(debug=True)
