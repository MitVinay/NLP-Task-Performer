from flask import (
    Flask, url_for, render_template
)


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title = "Home")

@app.route("/ner")
def ner():
    pass

if __name__ == "__main__":
    app.run(debug=True)