class Car:
    def __init__(self):
        self.name = None
        self.year = None
        self.color = None
        self.is_started = False
    def start_up(self):
        if self.is_started == False:
            print('Автомобиль заведен')
        else:
            print('Автомобиль уже был заведен')
    def shut_down(self):
        if self.is_started == True:
            print('Автомобиль заглушен')
        else:
            print('Автомобиль уже был заглушен')
    def set_color(self, color):
        self.color = color
    def set_name(self, name):
        self.name = name
    def set_year(self, year):
        self.year = year
    def show_stats(self):
        if self.name != None:
            print ('Имя:', self.name)
        else:
            print('Неизвестно')
        if self.color != None:
            print ('Цвет:', self.color)
        else:
            print('Неизвестно')
        if self.year != None:
            print ('Год выпуска:', self.year)
        else:
            print('Неизвестно')
car1 = Car()
car1.set_name('Машинка')
car1.set_color('Красный')
car1.set_year(2000)
car1.shut_down()
car1.start_up()
car1.start_up()
car1.shut_down()
car1.show_stats()
car1.set_year(2045)
car1.show_stats()