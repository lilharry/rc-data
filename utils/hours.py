import sqlite3
import os
import csv
import random

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

    reader = list(csv.reader(f1314))

    #stuff to generate random number for id
    l = range(len(reader))
    random.shuffle(l)
    i = 0

    for row in reader:
        try:
            student = row[0]
            if student[0:1] == "9":
                grade = 2014
            elif student[0:1] == "1":
                grade = 2015
            elif student[0:1] == "2":
                grade = 2016
            elif student[0:1] == "3":
                grade = 2017 
            student = int(student) #check if its an int, if not, go to except block
            student = l[i]
            hours = int(round(float(row[1]))) 
            if hours < 0:
                hours = 0
            h1314.append([student,hours,grade])

        except ValueError:
            pass
        i+=1

    reader = list(csv.reader(f1415))

    #stuff to generate random number for id
    l = range(len(reader))
    random.shuffle(l)
    i = 0

    for row in reader:
        try:
            student = row[0]
            if student[0:1] == "1":
                grade = 2015
            elif student[0:1] == "2":
                grade = 2016
            elif student[0:1] == "3":
                grade = 2017
            elif student[0:1] == "4":
                grade = 2018 
            student = int(student)
            student = l[i]
            hours = int(round(float(row[1])))
            if hours < 0:
                hours = 0
            h1415.append([student,hours,grade])
        
        except ValueError:
            pass
        i+=1

    reader = list(csv.reader(f1516))
    #stuff to generate random number for id
    l = range(len(reader))
    random.shuffle(l)
    i = 0

    for row in reader:
        try:
            student = row[0]
            if student[0:1] == "2":
                grade = 2016
            elif student[0:1] == "3":
                grade = 2017
            elif student[0:1] == "4":
                grade = 2018
            elif student[0:1] == "5":
                grade = 2019 
            student = int(student)
            student = l[i]
            hours = int(round(float(row[1])))
            if hours < 0:
                hours = 0
            h1516.append([student,hours,grade])
        except ValueError:
            pass
        i+=1

    reader = list(csv.reader(f1617))
    
    #stuff to generate random number for id
    l = range(len(reader))
    random.shuffle(l)
    i = 0

    for row in reader:
        try:
            student = row[0]
            if student[0:1] == "3":
                grade = 2017
            elif student[0:1] == "4":
                grade = 2018
            elif student[0:1] == "5":
                grade = 2019
            elif student[0:1] == "1":
                grade = 2020 
            student = int(student)
            student = l[i]
            hours = int(round(float(row[1])))
            if hours < 0:
                hours = 0
            h1617.append([student,hours,grade])          
    
        except ValueError:
            pass
        i+=1

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
        #connect to db
    db = sqlite3.connect("data/database.db")
    c = db.cursor()

    #open csvs
    f1314 = open("data/csv/hours_src-13-14.csv")
    f1415 = open("data/csv/hours_src-14-15.csv")
    f1516 = open("data/csv/hours_src-15-16.csv")
    f1617 = open("data/csv/hours_src-16-17.csv")
    
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

    reader = list(csv.reader(f1314))

    #stuff to generate random number for id
    l = range(len(reader))
    random.shuffle(l)
    i = 0

    for row in reader:
        try:
            student = row[0]
            if student[0:1] == "9":
                grade = 2014
            elif student[0:1] == "1":
                grade = 2015
            elif student[0:1] == "2":
                grade = 2016
            elif student[0:1] == "3":
                grade = 2017 
            student = int(student) #check if its an int, if not, go to except block
            student = l[i]
            hours = int(round(float(row[1])))
            if hours < 0:
                hours = 0
            h1314.append([student,hours,grade])

        except ValueError:
            pass
        i+=1
    
    reader = list(csv.reader(f1415))

    #stuff to generate random number for id
    l = range(len(reader))
    random.shuffle(l)
    i = 0

    for row in reader:
        try:
            student = row[0]
            if student[0:1] == "1":
                grade = 2015
            elif student[0:1] == "2":
                grade = 2016
            elif student[0:1] == "3":
                grade = 2017
            elif student[0:1] == "4":
                grade = 2018 
            student = int(student)
            student = l[i]
            hours = int(round(float(row[1])))
            if hours < 0:
                hours = 0
            h1415.append([student,hours,grade])
        
        except ValueError:
            pass
        i+=1

    reader = list(csv.reader(f1516))
    
    #stuff to generate random number for id
    l = range(len(reader))
    random.shuffle(l)
    i = 0

    for row in reader:
        try:
            student = row[0]
            if student[0:1] == "2":
                grade = 2016
            elif student[0:1] == "3":
                grade = 2017
            elif student[0:1] == "4":
                grade = 2018
            elif student[0:1] == "5":
                grade = 2019 
            student = int(student)
            student = l[i]
            hours = int(round(float(row[1])))
            if hours < 0:
                hours = 0
            h1516.append([student,hours,grade])
            
        except ValueError:
            pass
        i+=1

    reader = list(csv.reader(f1617))
    
    #stuff to generate random number for id
    l = range(len(reader))
    random.shuffle(l)
    i = 0

    for row in reader:
        try:
            student = row[0]
            if student[0:1] == "3":
                grade = 2017
            elif student[0:1] == "4":
                grade = 2018
            elif student[0:1] == "5":
                grade = 2019
            elif student[0:1] == "1":
                grade = 2020 
            student = int(student)
            student = l[i]
            hours = int(round(float(row[1])))
            if hours < 0:
                hours = 0
            h1617.append([student,hours,grade])          
    
        except ValueError:
            pass
        i+=1

    for student in h1314:
        c.execute("INSERT INTO rcids1314 VALUES (?,?,?)",(student[0],student[1],student[2]))
    for student in h1415:
        c.execute("INSERT INTO rcids1415 VALUES (?,?,?)",(student[0],student[1],student[2]))
    for student in h1516:
        c.execute("INSERT INTO rcids1516 VALUES (?,?,?)",(student[0],student[1],student[2]))
    for student in h1617:
        c.execute("INSERT INTO rcids1617 VALUES (?,?,?)",(student[0],student[1],student[2]))
    
    f1314.close()
    f1415.close()
    f1516.close()
    f1617.close()

    db.commit()
    db.close()


def getRandomRc():
    db = sqlite3.connect("data/database.db")
    c = db.cursor()
    
    query = "SELECT * FROM rcids1314,rcids1415,rcids1516,rcids1617 WHERE rcids1314.id = rcids1415.id AND rcids1415.id = rcids1516.id AND rcids1516.id = rcids1617.id"


    info = list(c.execute(query))
    random.shuffle(info)
    info = info[0]
    
    return {"id": info[0],
            "hours": [info[1],info[4],info[7],info[10]]
           }

def getRandomKc():
    db = sqlite3.connect("data/database.db")
    c = db.cursor()
    
    query = "SELECT * FROM kcids1314,kcids1415,kcids1516,kcids1617 WHERE kcids1314.id = kcids1415.id AND kcids1415.id = kcids1516.id AND kcids1516.id = kcids1617.id"


    info = list(c.execute(query))
    random.shuffle(info)
    info = info[0]
    
    return {"id": info[0],
            "hours": [info[1],info[4],info[7],info[10]]
           }
def getTotalRcHours():
    pass
def getTotalKcHours():
    pass

if __name__ == "__main__":
    '''    db = sqlite3.connect("data/database.db")
    c = db.cursor()

    query = "SELECT * FROM rcids1314,rcids1415,rcids1516,rcids1617 WHERE rcids1314.id = rcids1415.id AND rcids1415.id = rcids1516.id AND rcids1516.id = rcids1617.id"

    info = list(c.execute(query))
    random.shuffle(info)
    print info[0]
    '''
