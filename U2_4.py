class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def stats(self):
        return (self.name, self.age)

class ToyTarier(Dog):
    voice = 'loud'
    bred = 'ToyTarier'

class Spaniel(Dog):
    voice = 'quite'
    bred = 'Spaniel'

class GermanOvcharka(Dog):
    voice = 'playful'
    bred = 'GermanOvcharka'

dogs =  [None for i in range(6)]
names = ['GoodBoy', 'Pesik', 'VeryGoodBoy', 'AmazingBoy', 'Sobachka', 'Bobik']
for i in range(6):
    if i % 3 == 0:
        dogs[i] = ToyTarier(names[i], 1 + i)
    elif i % 3 == 1:
        dogs[i] = Spaniel(names[i], 1 + i)
    else:
        dogs[i] = GermanOvcharka(names[i], 1 + i)
    print(dogs[i].name, dogs[i].bred, dogs[i].voice, 'voice', dogs[i].age, 'years old', sep=', ')
