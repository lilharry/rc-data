import sqlite3
import os
import csv

def addKcidsToDb():
    db = sqlite3.connect("data/database.db")
    c = db.cursor()
    f = open("data/csv/kcids.csv")
    reader = csv.reader(f)
    for row in reader:
        try:
            student = row[0]
            if student[0:1] == "1":
                grade = 2020
            elif student[0:1] == "5":
                grade = 2029
            elif student[0:1] == "4":
                grade = 2018
            elif student[0:1] == "3":
                grade = 2017    
            hours = int(row[1])
            c.execute("INSERT INTO kcids VALUES (?,?,?)",(student,hours,grade))
            
        except ValueError:
            continue

    f.close()

    db.commit()
    db.close()

def addRcidsToDb():
    db = sqlite3.connect("data/database.db")
    c = db.cursor()
    f = open("data/csv/rcids.csv")
    reader = csv.reader(f)
    for row in reader:
        try:
            student = row[0]
            if student[0:1] == "1":
                grade = 2020
            elif student[0:1] == "5":
                grade = 2029
            elif student[0:1] == "4":
                grade = 2018
            elif student[0:1] == "3":
                grade = 2017    
            student = int(student)
            hours = int(row[1])
            c.execute("INSERT INTO kcids VALUES (?,?,?)",(student,hours,grade))
            
        except ValueError:
            continue

    f.close()

    db.commit()
    db.close()






