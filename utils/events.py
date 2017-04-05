import sqlite3
import os
import csv
import random

def addEventsToDb():
    db = sqlite3.connect("data/database.db")
    c = db.cursor()

    fe2016 = open("data/csv/src_events-select1516.csv")
    fe2017 = open("data/csv/src_events-select1617.csv")

    e2016 = []
    e2017 = []

    events = csv.reader(fe2016)
    for event in events:
        date = event[0]
        name = event[1]
        length = event[2]
        volunteers = event[3]
        if volunteers == "":
            volunteers = 0
        e2016.append([date,name,length,volunteers])

    events = csv.reader(fe2017)
    for event in events:
        date = event[0]
        name = event[1]
        length = event[2]
        volunteers = event[3]
        if volunteers == "":
            volunteers = 0
        e2017.append([date,name,length,volunteers])

    for e in e2016:
        c.execute("INSERT INTO rcevents2016 VALUES (?,?,?,?)",(e[0],e[1],e[2],e[3]))
    for e in e2017:
        c.execute("INSERT INTO rcevents2017 VALUES (?,?,?,?)",(e[0],e[1],e[2],e[3]))

    db.commit()
    db.close()

def fetchEvents():



if __name__ == "__main__":