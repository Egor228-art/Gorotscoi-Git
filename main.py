from flask import Flask, render_template, url_for
import sqlite3

app = Flask(__name__)

#БД
with sqlite3.connect("db/database.db") as db:
    cursor = db.cursor()
    pass

#Сайт
@app.route("/")
def index():
    print(url_for("index"))
    return render_template("index.html", title="Городской гид")

@app.route("/about")
def about():
    print(url_for("about"))
    return render_template("about.html", title="О сайте")

@app.route("/Restaurant")
def Restaurant():
    print(url_for("Restaurant"))
    return render_template("Restaurant.html", title="Рестораны")

@app.route("/Coffee")
def Coffee():
    print(url_for("Coffee"))
    return render_template("Coffee.html", title="Кафе")

if __name__ == "__main__":
    app.run(debug=True)