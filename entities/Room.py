class Room:
    def __init__(self):
        self.roomId = 0
        self.roomNo = 0
        self.roomType = ""
        self.t_desks = 0
        self.t_chairs = 0

    def setRoomNo(self, roomno):
        self.roomNo = roomno

    def getRoomNo(self):
        return self.roomNo

    def setRoomType(self, roomtype):
        self.roomType = roomtype

    def getRoomType(self):
        return self.roomType

    def sett_chairs(self, tchairs):
        self.t_chairs = tchairs

    def gett_chairs(self):
        return self.t_chairs

    def sett_desks(self, tdesks):
        self.t_desks = tdesks

    def gett_desks(self):
        return self.t_desks
    
    def addChair(self):
        self.t_chairs=self.t_chairs+1

    def addDesk(self):
        self.t_desks = self.t_desks + 1