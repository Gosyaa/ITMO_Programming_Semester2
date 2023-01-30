class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return (self.a + self. b)
    def multiplication(self):
        return (self.a * self.b)
    def division(self):
        if self.b != 0:
            return (self.a / self.b)
        else:
            return 'error'
    def subtraction(self):
        return (self.a - self.b)
a, b = map(int, input().split())
calc =  Math(a, b)
print(calc.addition())
print(calc.subtraction())
print(calc.multiplication())
print(calc.division())