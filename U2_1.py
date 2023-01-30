class Student:
    def __inint__(self):
        self.name = 'Radomir'
        self.age = 18
        self.groupNumber = 1213
    def setNameAge(self, name, age):
        self.name = name
        self.age = age
    def setGroupNumber(self, group):
        self.groupNumber = group
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getGroupNumber(self):
        return self.groupNumber
st = [Student() for i in range(5)]
names = ['Ivan', 'Gleb', 'Fedor', 'Daria', 'Alex']
for i in range(5):
    st[i].setNameAge(names[i], 17 + i)
    st[i].setGroupNumber(1215 + i)
print(st[0].getName())
print(st[2].getAge())
print(st[4].getGroupNumber())