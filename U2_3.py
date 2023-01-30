class Games:
    year = 1970
    def __init__(self):
        self.name = ''
    def setname(self, name):
        self.name = name
    def getname(self):
        if self.name == '':
            return 'error'
        else:
            print(self.name)
    def setyear(self, game_year):
        self.year = game_year

class PS4Games(Games):
    platform = 'PS4'
    def getName(self):
        print('This is PS4 game')
        if self.name == '':
            return 'error'
        else:
            return(self.name)

class XboxGames(Games):
    platform = 'Xbox'
    def getName(self):
        print('This is Xbox game')
        if self.name == '':
            return 'error'
        else:
            return(self.name)

class PCGames(Games):
    platform = 'PC'
    def getName(self):
        print('This is PC game')
        if self.name == '':
            return 'error'
        else:
            return(self.name)

class MobileGames(Games):
    platform = 'Mobile'
    def getName(self):
        print('This is mobile game')
        if self.name == '':
            return 'error'
        else:
            return(self.name)

g1 = PS4Games()
g2 = XboxGames()
g3 = PCGames()
g4 = MobileGames
g1.setyear(2018)
print(g1.year)
g3.setname('Tetris')
print(g3.getName())
