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
    db = sqlite3.connect("data/database.db")
    c = db.cursor()
    
             #j,f,m,a,m,j,j,a,s,o,n,d
    e2016h = [0,0,0,0,0,0,0,0,0,0,0,0]
    e2016v = [0,0,0,0,0,0,0,0,0,0,0,0]
    e2017h = [0,0,0,0,0,0,0,0,0,0,0,0]  
    e2017v = [0,0,0,0,0,0,0,0,0,0,0,0]  

    query = "SELECT * FROM rcevents2016"
    
    events = c.execute(query)
    for e in events:
        month = int(e[0][:2]) 
        hours = e[2] / 60.0
        volunteers = e[3]
        e2016h[month - 1] += hours * volunteers
        e2016v[month - 1] += volunteers
    
    query = "SELECT * FROM rcevents2017"
    
    events = c.execute(query)
    for e in events:
        month = int(e[0][:2]) 
        hours = e[2] / 60.0 
        volunteers = e[3]
        e2017h[month - 1] += hours * volunteers
        e2017v[month - 1] += volunteers

    db.close()

    return {"e2016h":e2016h,
            "e2017h":e2017h,
            "e2016v":e2016v,
            "e2017v":e2017v} 



#mm -> name
def monthConversion(mm):
    months = ["January","February","March",
              "April","May","June","July",
              "August","September","October",
              "November","December"]    
    return months[int(mm)-1]

#hrs per month
#events per month

if __name__ == "__main__":
    print fetchEvents()