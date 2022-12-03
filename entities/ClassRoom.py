class ClassRoom:
    def __init__(self):
        self.cr_type=""
        self.t_capacity=0
        self.t_furniture=0
        self.f_contition=0

    def setcr_type(self , crtype):
        self.cr_type=crtype
    
    def getcr_type(self):
        return self.cr_type

    def sett_capacity(self, crtype):
        self.t_capacity = crtype

    def gett_capacity(self):
        return self.t_capacity

    def sett_furniture(self, crtype):
        self.t_furniture = crtype

    def gett_furniture(self):
        return self.t_furniture

    def addfurniture(self):
        self.t_furniture = self.t_furniture + 1

    def increaseCapacity(self):
        self.t_capacity = self.t_capacity + 1
    

