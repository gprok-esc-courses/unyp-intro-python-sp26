
class Rectangle:
    def __init__(self, w, h):
        self.width = 0
        self.height = 0
        self.set_width(w)
        self.set_height(h)

    def __str__(self):
        return f"Rectangle, width {self.width}, height {self.height}"
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def set_width(self, w):
        if w > 0:
            self.width = w 

    def set_height(self, h):
        if h > 0:
            self.height = h



if __name__ == '__main__':
    a = Rectangle(10, 5)
    b = Rectangle(4, 3)

    print(a)
    print(a.area())
    print(a.perimeter())
    print(b)
    print(b.area())
    print(b.perimeter())