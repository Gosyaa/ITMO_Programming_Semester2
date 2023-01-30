class Country:
    def __init__(self):
        pass

class Russia(Country):
    capital = 'Moscow'
    def __init__(self):
        self.population = None
    def setPopulation(self, population):
        self.population = population
    def getPopulation(self):
        if self.population == None:
            return 'error'
        else:
            return self.population
class Canada(Country):
    capital = 'Ottawa'
    def __init__(self):
        self.population = None
    def setPopulation(self, population):
        self.population = population
    def getPopulation(self):
        if self.population == None:
            return 'error'
        else:
            return self.population

class Germany(Country):
    capital = 'Berlin'
    def __init__(self):
        self.population = None
    def setPopulation(self, population):
        self.population = population
    def getPopulation(self):
        if self.population == None:
            return 'error'
        else:
            return self.population

r1 = Russia()
print(r1.getPopulation())
r1.setPopulation(45544646)
c1 = Canada()
c1.setPopulation(7865321)
g1 = Germany()
g1.setPopulation(1219787451321)
print(c1.getPopulation())