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
                grade = 4
            elif student[0:1] == "1":
                grade = 3
            elif student[0:1] == "2":
                grade = 2
            elif student[0:1] == "3":
                grade = 1
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
                grade = 4
            elif student[0:1] == "2":
                grade = 3
            elif student[0:1] == "3":
                grade = 2
            elif student[0:1] == "4":
                grade = 1 
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
                grade = 4
            elif student[0:1] == "3":
                grade = 3
            elif student[0:1] == "4":
                grade = 2
            elif student[0:1] == "5":
                grade = 1
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
                grade = 4
            elif student[0:1] == "4":
                grade = 3
            elif student[0:1] == "5":
                grade = 2
            elif student[0:1] == "1":
                grade = 1
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
                grade = 4
            elif student[0:1] == "1":
                grade = 3
            elif student[0:1] == "2":
                grade = 2
            elif student[0:1] == "3":
                grade = 1
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
                grade = 4
            elif student[0:1] == "2":
                grade = 3
            elif student[0:1] == "3":
                grade = 2
            elif student[0:1] == "4":
                grade = 1
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
                grade = 4
            elif student[0:1] == "3":
                grade = 3
            elif student[0:1] == "4":
                grade = 2
            elif student[0:1] == "5":
                grade = 1
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
                grade = 4
            elif student[0:1] == "4":
                grade = 3
            elif student[0:1] == "5":
                grade = 2
            elif student[0:1] == "1":
                grade = 1
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

    db.close()
    
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
    
    db.close()

    return {"id": info[0],
            "hours": [info[1],info[4],info[7],info[10]]
           }
def getTotalRcHours():
    db = sqlite3.connect("data/database.db")
    c = db.cursor()
    
    #hrs  = [f,s,j,S]
    h1314 = [0,0,0,0]
    h1415 = [0,0,0,0]
    h1516 = [0,0,0,0]
    h1617 = [0,0,0,0]
        
    info = c.execute("SELECT hours,grade from rcids1314")

    for x in info:
        grade = x[1]
        if grade == 1:
            h1314[0] += x[0]
        elif grade == 2:
            h1314[1] += x[0]
        elif grade == 3:
            h1314[2] += x[0]
        elif grade == 4:
            h1314[3] += x[0]
    
    info = c.execute("SELECT hours,grade from rcids1415")

    for x in info:
        grade = x[1]
        if grade == 1:
            h1415[0] += x[0]
        elif grade == 2:
            h1415[1] += x[0]
        elif grade == 3:
            h1415[2] += x[0]
        elif grade == 4:
            h1415[3] += x[0]
    
    info = c.execute("SELECT hours,grade from rcids1516")

    for x in info:
        grade = x[1]
        if grade == 1:
            h1516[0] += x[0]
        elif grade == 2:
            h1516[1] += x[0]
        elif grade == 3:
            h1516[2] += x[0]
        elif grade == 4:
            h1516[3] += x[0]
    
    info = c.execute("SELECT hours,grade from rcids1617")

    for x in info:
        grade = x[1]
        if grade == 1:
            h1617[0] += x[0]
        elif grade == 2:
            h1617[1] += x[0]
        elif grade == 3:
            h1617[2] += x[0]
        elif grade == 4:
            h1617[3] += x[0]
    
    db.close()
    return {"2014":h1314,
            "2015":h1415,
            "2016":h1516,
            "2017":h1617}




def getTotalKcHours():
    db = sqlite3.connect("data/database.db")
    c = db.cursor()
    
    #hrs  = [f,s,j,S]
    h1314 = [0,0,0,0]
    h1415 = [0,0,0,0]
    h1516 = [0,0,0,0]
    h1617 = [0,0,0,0]
        
    info = c.execute("SELECT hours,grade from kcids1314")

    for x in info:
        grade = x[1]
        if grade == 1:
            h1314[0] += x[0]
        elif grade == 2:
            h1314[1] += x[0]
        elif grade == 3:
            h1314[2] += x[0]
        elif grade == 4:
            h1314[3] += x[0]
    
    info = c.execute("SELECT hours,grade from kcids1415")

    for x in info:
        grade = x[1]
        if grade == 1:
            h1415[0] += x[0]
        elif grade == 2:
            h1415[1] += x[0]
        elif grade == 3:
            h1415[2] += x[0]
        elif grade == 4:
            h1415[3] += x[0]
    
    info = c.execute("SELECT hours,grade from kcids1516")

    for x in info:
        grade = x[1]
        if grade == 1:
            h1516[0] += x[0]
        elif grade == 2:
            h1516[1] += x[0]
        elif grade == 3:
            h1516[2] += x[0]
        elif grade == 4:
            h1516[3] += x[0]
    
    info = c.execute("SELECT hours,grade from kcids1617")

    for x in info:
        grade = x[1]
        if grade == 1:
            h1617[0] += x[0]
        elif grade == 2:
            h1617[1] += x[0]
        elif grade == 3:
            h1617[2] += x[0]
        elif grade == 4:
            h1617[3] += x[0]
    db.close()
    return {"2014":h1314,
            "2015":h1415,
            "2016":h1516,
            "2017":h1617}

def getTotalVolunteers():
    db = sqlite3.connect("data/database.db")
    c = db.cursor()
    for x in c.execute("SELECT COUNT(*) FROM rcids1314"):
        rc2014 = x[0]
    for x in c.execute("SELECT COUNT(*) FROM rcids1415"):
        rc2015 = x[0]
    for x in c.execute("SELECT COUNT(*) FROM rcids1516"):
        rc2016 = x[0]
    for x in c.execute("SELECT COUNT(*) FROM rcids1617"):
        rc2017 = x[0]
    for x in c.execute("SELECT COUNT(*) FROM kcids1314"):
        kc2014 = x[0]
    for x in c.execute("SELECT COUNT(*) FROM kcids1415"):
        kc2015 = x[0]
    for x in c.execute("SELECT COUNT(*) FROM kcids1516"):
        kc2016 = x[0]
    for x in c.execute("SELECT COUNT(*) FROM kcids1617"):
        kc2017 = x[0]
    
    db.close()
    return {"rc2014":rc2014,
            "rc2015":rc2015,
            "rc2016":rc2016,
            "rc2017":rc2017,
            "kc2014":kc2014,
            "kc2015":kc2015,
            "kc2016":kc2016,
            "kc2017":kc2017}


if __name__ == "__main__":
    '''    db = sqlite3.connect("data/database.db")
    c = db.cursor()

    query = "SELECT * FROM rcids1314,rcids1415,rcids1516,rcids1617 WHERE rcids1314.id = rcids1415.id AND rcids1415.id = rcids1516.id AND rcids1516.id = rcids1617.id"

    info = list(c.execute(query))
    random.shuffle(info)
    print info[0]
    '''
    print getTotalVolunteers()
    