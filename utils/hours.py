import sqlite3
import os
import csv

def addKcidsToDb():
    #connect to db
    db = sqlite3.connect("data/database.db")
    c = db.cursor()

    #open csvs
    f1314 = open("data/csv/hours_kc-13-14.csv")
    f1415 = open("data/csv/hours_kc-14-15.csv")
    f1516 = open("data/csv/hours_kc-15-16.csv")
    f1617 = open("data/csv/hours_kc-16-17.csv")
    
    #id correspondence
    #YY - YY f s j S
    #13 - 14 3 2 1 9
    #14 - 15 4 3 2 1
    #15 - 16 5 4 3 2
    #16 - 17 1 5 4 3

    #arrays
    h1314 = []
    h1415 = []
    h1516 = []
    h1617 = []

    reader = csv.reader(f1314)
    for row in reader:
        try:
            student = row[0]
            if student[0:1] == "9":
                grade = 4
            elif student[0:1] == "1":
                grade = 3
            elif student[0:1] == "2":
                grade = 2
            elif student[0:1] == "3":
                grade = 1    
            hours = int(row[1])

            h1314.append(student,hours,grade)

        except ValueError:
            continue
    
    reader = csv.reader(f1415)
    for row in reader:
        try:
            student = row[0]
            if student[0:1] == "1":
                grade = 4
            elif student[0:1] == "2":
                grade = 3
            elif student[0:1] == "3":
                grade = 2
            elif student[0:1] == "4":
                grade = 1    
            hours = int(row[1])

            h1415.append(student,hours,grade)
        
        except ValueError:
            continue

    reader = csv.reader(f1516)
    for row in reader:
        try:
            student = row[0]
            if student[0:1] == "2":
                grade = 4
            elif student[0:1] == "3":
                grade = 3
            elif student[0:1] == "4":
                grade = 2
            elif student[0:1] == "5":
                grade = 1    
            hours = int(row[1])

            h1516.append(student,hours,grade)
            
        except ValueError:
            continue

    reader = csv.reader(f1617)
    for row in reader:
        try:
            student = row[0]
            if student[0:1] == "3":
                grade = 4
            elif student[0:1] == "4":
                grade = 3
            elif student[0:1] == "5":
                grade = 2
            elif student[0:1] == "1":
                grade = 1    
            hours = int(row[1])
        
            h1617.append(student,hours,grade)          
    
        except ValueError:
            continue

    for student in h1314:
        c.execute("INSERT INTO kcids1314 VALUES (?,?,?)",(student[0],student[1],student[2]))
    for student in h1415:
        c.execute("INSERT INTO kcids1415 VALUES (?,?,?)",(student[0],student[1],student[2]))
    for student in h1516:
        c.execute("INSERT INTO kcids1516 VALUES (?,?,?)",(student[0],student[1],student[2]))
    for student in h1617:
        c.execute("INSERT INTO kcids1617 VALUES (?,?,?)",(student[0],student[1],student[2]))
    
    f1314.close()
    f1415.close()
    f1516.close()
    f1617.close()

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

    db.commit()
    db.close()






