rom flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:''@localhost/naven'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

"""app.config.update(
    TESTING=True,
    SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/'
)"""
db = SQLAlchemy(app)

class Location(db.Model):
    Location_id = db.Column(db.Integer, primary_key= True)
    def __repr__(self):
        return f"Location('{self.Location_id}')"

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key= True)
    def __repr__(self):
        return f"Product('{self.Product_id}')"

class ProductMovement(db.Model):
    Movement_id = db.Column(db.Integer, primary_key= True)
    TimeStamp = db.Column(db.DateTime, default=datetime.utcnow)
    From_Location = db.Column(db.String(20), nullable = False)
    To_Location = db.Column(db.String(20), nullable = False)
    Product_id= db.Column(db.Integer)
    Product_qnty= db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"ProductMovement('{self.Movement_id}','{self.TimeStamp}','{self.From_Location}','{self.To_Location}','{self.Product_id}','{self.Product_qnty}')"
