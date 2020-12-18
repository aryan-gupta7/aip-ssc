from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("title_page.html")

@app.route("/acknowledgement")
def ack():
    return render_template("acknowledgement.html")

@app.route("/climate-of-sikkim")
def climate():
    return render_template("page2.html")

@app.route("/winter")
def winter():
    return render_template("winter.html")

@app.route("/summer")
def summer():
    return render_template("summer.html")

@app.route("/monsoon")
def monsoon():
    return render_template("monsoon.html")

if __name__ == "__main__":
    app.run(debug=True)