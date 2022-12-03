
class University:
    
    def __init__(self):
        self.name = ""
        self.address = ""
        self.uniId=0


    def setName(self,name):
        self.name=name
    
    def getName(self):
        return self.name

    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address

    def setUniId(self, uniId):
        self.uniId = uniId

    def getUniId(self):
        return self.uniId
