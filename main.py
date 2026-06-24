from flask import Flask, request,render_template

app = Flask(__name__, template_folder="template", static_folder="static")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["POST"])
def login():

    email = request.form.get("email")
    password = request.form.get("password")

    return f"""
    Email : {email}
    Password : {password}
    """

@app.route("/dashb")
def dashboard():
    return render_template("dashboard.html")


@app.route("/reg", methods=["POST"])
def register():

    fullname = request.form.get("fullname")
    email = request.form.get("email")
    password = request.form.get("password")

    return f"""
    Name : {fullname}
    Email : {email}
    Password : {password}
    """

if __name__=="__main__":
    app.run(debug=True)
