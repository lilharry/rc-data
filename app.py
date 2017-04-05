from flask import Flask, render_template, url_for
from utils import hours,events
import os
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('main.html')

@app.route("/events")
def events():
    return render_template('events.html',e = hours.fetchEvents())


if __name__ == '__main__':
    if os.path.getsize("data/database.db") == 0:
        f = "data/database.db"
        db = sqlite3.connect(f, check_same_thread=False)
        c = db.cursor()
        print "Initializing database"
        c.execute("CREATE TABLE rcids1314 (id INTEGER, hours INTEGER, grade INTEGER)")
        c.execute("CREATE TABLE rcids1415 (id INTEGER, hours INTEGER, grade INTEGER)")
        c.execute("CREATE TABLE rcids1516 (id INTEGER, hours INTEGER, grade INTEGER)")
        c.execute("CREATE TABLE rcids1617 (id INTEGER, hours INTEGER, grade INTEGER)")

        c.execute("CREATE TABLE rcevents2016 (name TEXT, date TEXT, length INTEGER, volunteers INTEGER )")
        c.execute("CREATE TABLE rcevents2017 (name TEXT, date TEXT, length INTEGER, volunteers INTEGER )")  

        c.execute("CREATE TABLE kcids1314 (id INTEGER, hours INTEGER, grade INTEGER)")
        c.execute("CREATE TABLE kcids1415 (id INTEGER, hours INTEGER, grade INTEGER)")
        c.execute("CREATE TABLE kcids1516 (id INTEGER, hours INTEGER, grade INTEGER)")
        c.execute("CREATE TABLE kcids1617 (id INTEGER, hours INTEGER, grade INTEGER)")
        
        events.addEventsToDb()
        hours.addRcidsToDb()
        hours.addKcidsToDb()
        
        db.commit()
        db.close()
    app.debug = True
    app.secret_key = '  \x43\xd2\x34\x92\x5b\x4a\x80\xfc\xc6\xb0\x0e\x45\xdd\x51\x36\xc0\xd2\x3a\x85\x42\x57\xbb\x61\xf2\x7b\xb6\xfc\x17\x3b\x1a\xda\x5b\x6d\x7d\x0a\xff\xd3\x6f\xfa\x7c\x1b\xa8\x0f\x7f\x53\x18\x8d\x91\x16\x81'
    app.run()
