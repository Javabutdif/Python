from flask import Flask, render_template
from dbhelper import *

	

app = Flask(__name__)

@app.route("/")

def main()->None:
	
	studentlist = getrecord("students")
	return render_template("index.html", title = "student List", slist= studentlist)
	
	
if __name__ == "__main__":
	app.run(debug=True)