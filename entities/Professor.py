from entities.Person import Person


class Professor(Person):
    def __init__(self):
        self.type=""
        self.qualification=""
        self.department=""
        self.y_experience=0
        
    def setVals(self,name,email,salary,contact,room,dept):
        self.name=name
        self.email=email
        self.contact_no=contact
        self.room=room
        self.department=dept
        self.salary=salary

    def setType(self,type):
        self.type=type
    
    def getType(self):
        return self.type

    def setqualification(self, qualification):
        self.qualification = qualification

    def getqualification(self):
        return self.qualification

    def sety_experience(self, y_experience):
        self.y_experience = y_experience

    def gety_experience(self):
        return self.y_experience

    def setdepartment(self, department):
        self.department = department

    def getdepartment(self):
        return self.department

    def toString(self):
        return ",".join([self.name,self.email,str(self.salary),self.contact_no,str(self.room),self.department])

