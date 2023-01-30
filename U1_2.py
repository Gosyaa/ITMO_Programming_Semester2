class Soda:
    def __init__(self, extra):
        self.extra = extra
    def show_my_drink(self):
        print('Газировка и', self.extra)
syrup = Soda('сахар')
syrup.show_my_drink()