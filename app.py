from flask import Flask, render_template, request
from wtforms import Form, TextField, IntegerField, RadioField, validators
from wtforms.fields.html5 import EmailField 
import requests
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_super_secret_key'

@app.route('/')
@app.route("/home")
def hello_world():
    return '<h1> Hello, World! </h1>'
	
@app.route("/contact")
def contact_page():
	gh_link = "https://github.com/weiernt"
	
	
	return render_template("contact_page.html", gh_link=gh_link)
	
class MySearchForm(Form):
	iso = TextField("iso: ", validators=[validators.DataRequired()])
	region_province = TextField("province: ", validators=[validators.DataRequired()])
	
	
@app.route("/search", methods=["GET", "POST"])
def search_page():
	print(request.form)
	form = MySearchForm(request.form)
	# iso=region_province=False
	search_results=False
	
	if request.method=="POST":
		iso = request.form["iso"]
		region_province = request.form["region_province"]
		
		if form.validate():
			search_results = make_request(iso, region_province)
	return render_template("search_page.html", form=form, search_results=search_results)
		
def make_request(iso, region_province):
	url = "https://covid-api.com/api/reports"
	url = url + f"?iso={iso}&region_province={region_province}"
	r = requests.request("GET", url)
	return json.loads(r.text)
	

if __name__=="__main__":
	app.run(debug=True)
	
