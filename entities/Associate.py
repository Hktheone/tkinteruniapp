from entities.Professor import Professor


class Associate(Professor):
    def __init__(self):
        self.assoc_Experience = 0
        self.yearly_increment = 0

    def setAssocExpereince(self, experience):
        self.assoc_Experience = experience

    def getAssocExpereince(self):
        return self.assoc_Experience

    def setYearlyIncrement(self, increment):
        self.yearly_increment = increment

    def getYearlyIncrement(self):
        return self.yearly_increment

    def addExperience(self):
        self.assoc_Experience = self.assoc_Experience + 1

    def giveIncrement(self):
        self.yearly_increment=self.yearly_increment+1
