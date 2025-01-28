
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

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
      name=request.form["name"]
      email=request.form["email"]
      phone=request.form["phone"]
      #print(request.form)
      events=[]
      if request.form.get("event1"):
        events.append(request.form.get("event1"))
      if request.form.get("event2"):
        events.append(request.form.get("event2"))
      if request.form.get("event3"):
        events.append(request.form.get("event3"))
    #   print(name,email,phone,events) 
      participant=Participant(Name=name,Email=email,Phone_no=phone,Events=events)
      db.session.add(participant)
      db.session.commit()
      data="Registration Successful" 
      return render_template("home.html",data=data, name=name, email=email, phone=phone, events=events)
    return render_template("register.html")


if __name__=="__main__":
    app.run(debug=True)
