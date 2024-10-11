from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
db = SQLAlchemy(app)
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True,nullable=False)
    desc = db.Column(db.String(120))
    def __repr__(self):
        return f"{self.name} - {self.desc}"
    
@app.route('/')
def home():
    return "Hello, hi"
@app.route('/drinks')
def drinks():
    drs = Drink.query.all()
    output = []
    for drink in drs:
        output.append({'name': drink.name, 'desc': drink.desc})
    drinks = {"drinks": output}
    return drinks
@app.route('/drinks/<id>')
def drink(id):
    drink = Drink.query.get_or_404(id)
    return {"name": drink.name,"desc": drink.desc}

@app.route('/drinks',methods = ["POST"])
def add_drink():
    drink = Drink(name=request.json['name'],
                  desc=request.json['desc'])
    db.session.add(drink)
    db.session.commit()
    return {"id": drink.id}
@app.route('/drinks/<id>',methods = ["DELETE"])
def del_drink(id):
    drink = Drink.query.get(id)
    if not drink:
        return {"message": "Not found your drink"}
    db.session.delete(drink)
    db.session.commit()
    return {"message": "Yahoooooooooooooooo!"}