from flask import (
    Flask, url_for, render_template
)

from form import InputForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title = "Home")

@app.route("/ner", methods=["GET", "POST"])
def ner():
    form = InputForm()
    if form.validate_on_submit():
        airline = [form.airline.data]
        message = f"The Sentiment is {airline}"
    else:
        message = "Please provide valid input details!"
    return render_template("ner.html", title = "Named Entity Recoginition", form=form,
                           output=message)

if __name__ == "__main__":
    app.run(debug=True)