import os
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", page_title="Home | Coffee")

@app.route("/about")
def about():
    data = []
    with open("data/coffee.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About | Coffee", coffee=data)

@app.route("/about/<coffee_name>")
def about_coffee(coffee_name):
    coffee = {}
    with open("data/coffee.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == coffee_name:
                coffee = obj

    return render_template("coffee.html", cofefe=coffee)

@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact | Coffee")

@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers | Coffee")
    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)