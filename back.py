import sqlite3
from flask import Flask
from flask import g
from flask_sqlalchemy import SQLAlchemy
from user import *
from main import app
import copy 
from GoogleAPI import convertDist

# app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///info.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

db.Model.metadata.reflect(db.engine)

class Entry(db.Model):
    __tablename__ = 'users'
    __table_args__ = { 'extend_existing': True }
    usrid = db.Column(db.Integer, nullable=False, primary_key=True)  
    usrtype = db.Column(db.Text, nullable=False) 
    usrname = db.Column(db.Text, nullable=False) 
    spltype = db.Column(db.Text, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    addr = db.Column(db.Text, nullable=False)
    tel = db.Column(db.Integer, nullable=False)
    email = db.Column(db.Text, nullable=False)
    info = db.Column(db.Text, nullable=False)

def editEntry(user):
    entry = Entry.query.filter_by(usrid=user.uid).first()
    entry.number = copy.deepcopy(user.supplyNumber)
    db.session.commit()
    return "Entry changed"

def addEntry(user):
    usrid = Entry.query.count() + 1
    newEntry = Entry(usrid = usrid, 
                     usrtype = copy.deepcopy(user.type), 
                     usrname = copy.deepcopy(user.name),
                     spltype = copy.deepcopy(user.supplyType),
                     number = copy.deepcopy(user.supplyNumber),
                     addr = copy.deepcopy(user.addr),
                     tel = copy.deepcopy(user.tel),
                     email = copy.deepcopy(user.email),
                     info = copy.deepcopy(user.info))
    db.session.add(newEntry)
    db.session.commit()
    return "Entry added"

def entrytoUser(entry):
    newuser = User()
    uid = copy.deepcopy(entry.usrid)
    name = copy.deepcopy(entry.usrname)
    usrtype = copy.deepcopy(entry.usrtype)
    supplyType = copy.deepcopy(entry.spltype)
    supplyNumber = copy.deepcopy(entry.number)
    addr = copy.deepcopy(entry.addr)
    tel = copy.deepcopy(entry.tel)
    email = copy.deepcopy(entry.email)
    info = copy.deepcopy(entry.info)
    newuser.setAll(usrtype, name, supplyType, supplyNumber, addr, tel, email, info)
    newuser.setUid(uid)
    return newuser

# a list of tuples of [lat, lon] is returned
def returnLocList():
    locs = Entry.query.filter_by(spltype="donor").all()
    loccoor = [getCoord(entry.addr) for entry in locs]
    return loccoor

# A seeker type user object is passed in
# A usrid is returned
def returnClosestLoc(seeker):
    skaddr = seeker.addr
    locs = Entry.query.filter_by(usrtype="donor").all()
    usrids = [entry.usrid for entry in locs]
    addrs = [entry.addr for entry in locs]
    dics = { usrids[i] : addrs[i] for i in range(len(addrs))}
    print(len(dics))
    return findClosest(skaddr, dics)

# @app.route("/")
# def home():
#     # print("Total number of user entries is", Entry.query.count())
#     # return "Done"
#     # entry = Entry.query.filter_by(usrid=0).first()
#     # addEntry(entrytoUser(entry))
#     # return "Entry added"
#     seeker = User()
#     print(returnClosestLoc(seeker))
#     return Entry.query.filter_by(usrid = returnClosestLoc(seeker)).first().addr

# if __name__ == "__main__":
#     app.run(debug=True)