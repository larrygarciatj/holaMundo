from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
import os 

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "\\database\\database.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Posts(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(50))

@app.route("/")
def index():
	titulo = "home prueba"
	lista = range(1,10)
	return render_template("index.html",titulo=titulo,lista=lista)

if __name__ == "__main__":
	db.create_all()
	app.run(debug=True)