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
    

    f = open("static/e2016.csv","w")
    f.write("date,volunteers,hours\n")
    query = "SELECT * FROM rcevents2016"
    
    events = c.execute(query)
    dates = []
    volunteers = []
    hours = []
    i = -1
    date = ""
    for e in events:
        if date != e[0][:3] + e[0][6:]:
            dates.append(e[0][:3] + e[0][6:])
            volunteers.append(0)
            hours.append(0)
            i+=1
            date = dates[i]
        
        volunteers[i] += e[3]
        hours[i] += e[2] / 60.0 * e[3]   

    for i in range(len(dates)):

        f.write("%s,%s,%s\n"%(dates[i],volunteers[i],hours[i]))
    f.close()

    f = open("static/e2017.csv","w")
    f.write("date,volunteers,hours\n")
    query = "SELECT * FROM rcevents2017"
    
    events = c.execute(query)
    dates = []
    volunteers = []
    hours = []
    i = -1
    date = ""
    for e in events:
        if date != e[0][:3] + e[0][6:]:
            dates.append(e[0][:3] + e[0][6:])
            volunteers.append(0)
            hours.append(0)
            i+=1
            date = dates[i]
        
        volunteers[i] += e[3]
        hours[i] += e[2] / 60.0 * e[3]   

    for i in range(len(dates)):

        f.write("%s,%s,%s\n"%(dates[i],volunteers[i],hours[i]))
    f.close()
    db.close()
    
    return

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