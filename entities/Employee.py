from entities.Person import Person


class Employee(Person):
    def __init__(self):
        self.e_id=0
        self.e_title=""
        
    
    def setTitle(self,title):
        self.e_title=title
    
    def getTitle(self):
        return self.e_title

    def getId(self):
        return self.e_id
