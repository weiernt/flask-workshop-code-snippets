from flask import Flask, render_template
import requests
# import requests as r

app = Flask(__name__)
gh_link = "https://github.com/weiernt"
list_of_contacts = [gh_link, "https://facebook.com"]

@app.route("/")
@app.route("/home")
def hello():
    return render_template("home_page.html", links=list_of_contacts)

def make_request(iso):
    url = "https://covid-api.com/api/reports?"
    url = url + "iso=" + iso
    data = requests.request("GET", url)
    return data.json()

if __name__=="__main__":
    # print(make_request("AUS")["data"])
    app.run(debug=True)