from entities.Professor import Professor


class Assistant(Professor):
    def __init__(self):
        self.asst_experience=0
        self.yearly_increment=0
        
    
    def setAsstExpereince(self,experience):
        self.asst_Experience=experience
        

    def getAsstExpereince(self):
        return self.asst_Experience


    def setYearlyIncrement(self, increment):
        self.yearly_increment = increment

    def getYearlyIncrement(self):
        return self.yearly_increment


    def addExperience(self):
        self.asst_experience=self.asst_Experience+1

    def giveIncrement(self):
        self.yearly_increment=self.yearly_increment+1
