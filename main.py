from flask import Flask
from flask import render_template
app=Flask(__name__,template_folder="template", static_folder="static")#"__main__"#print(__name_)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dashb")
def dashboard():
    return render_template("dashboard.html")

@app.route("/reg")
def register():
    return render_template("register.html")


if __name__=="__main__":
    app.run(debug=True)