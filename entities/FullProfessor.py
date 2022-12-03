from entities.Professor import Professor


class FullProfessor(Professor):
    def __init__(self):
        self.fullprof_Experience = 0
        self.yearly_increment = 0

    def setFullProfExpereince(self, experience):
        self.fullprof_Experience = experience

    def getFullProfExpereince(self):
        return self.fullprof_Experience

    def setYearlyIncrement(self, increment):
        self.yearly_increment = increment

    def getYearlyIncrement(self):
        return self.yearly_increment

    def addExperience(self):
        self.FullProf_Experience = self.FullProf_Experience + 1

    def giveIncrement(self):
        self.yearly_increment=self.yearly_increment+1
