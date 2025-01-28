from flask import Flask , render_template , request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy()
#configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Event-Registration.db"
db.init_app(app)

class Participant(db.Model):
    __tablename__="Participants"
    ID=db.Column(db.Integer,primary_key=True)
    Name=db.Column(db.String,unique=False,nullable=False)
    Email=db.Column(db.String,unique=True,nullable=False)
    Phone_no=db.Column(db.Integer,unique=True,nullable=False)
    Events=db.Column(db.PickleType,unique=False,nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register")
def register():
    return render_template("register.html")


if __name__=="__main__":
    app.run(debug=True)