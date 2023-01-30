class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def square(self):
        return (self.width * self.height)
a, b = map(int, input().split())
rec = Rectangle(a, b)
print(rec.square())
