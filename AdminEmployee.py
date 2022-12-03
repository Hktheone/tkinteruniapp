import os

from entities.Professor import Professor
from entities.Student import Student


class AdminEmployee():
    def __init__(self):
        self.prof = []
        self.stud = []
        self.crPath = os.getcwd() + "\\pythonProject\\"
        self.readStudents()
        self.readProfessors()
        print("Data read")

    def readProfessors(self):
        with open(self.crPath + "profData.txt", "r") as file:
            for rows in file.read().split("\n"):
                row = rows.split(",")
                if (len(row) > 1):
                    p = Professor()
                    p.setVals(row[0], row[1], row[2], row[3], row[4], row[5])
                    self.prof.append(p)

    def readStudents(self):
        with open( self.crPath + "studData.txt", "r") as file:
            for rows in file.read().split("\n"):
                row = rows.split(",")

                if(len(row)>1):
                    s = Student()
                    s.setVals(row[0], row[1], row[2], row[3], row[4])
                    self.stud.append(s)
                    # print(s.toString())

    def save(self):
        with open(self.crPath + "studData.txt", "w") as file:
            for s in self.stud:
                #print(s.toString())
                file.write(s.toString()+"\n")

        with open(self.crPath + "profData.txt", "w") as file:
            for p in self.prof:
                #print(p.toString())
                file.write(p.toString() + "\n")

        print("Data Written Successfully")



