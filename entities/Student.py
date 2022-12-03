

class Student():
    def __init__(self):
        self.credits=0
        self.t_credits=0
        self.department=0
        self.course=""
        self.name=""
        self.email=""

    def setVals(self,name,email,course,department,t_credits):

        self.name=name
        self.email=email
        self.course=course
        self.department=department
        self.t_credits= int(t_credits)

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email
        
    def setCourse(self,course):
        self.course=course
    
    def getCourse(self):
        return self.course

    def setDepartment(self, department):
        self.department = department

    def getDepartment(self):
        return self.department

    def sett_Credits(self, t_credits):
        self.t_credits = t_credits

    def gett_Credits(self):
        return self.t_credits

    def toString(self):
        return ",".join([self.name,self.email,self.course,self.department,str(self.t_credits)])