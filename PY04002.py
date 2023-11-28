class Rectangle:
    def __init__(self, length, width, c):
        self.length = length
        self.width = width
        self.c = c
    
    def area(self):
        return self.width * self.length

    def perimeter(self):
        return (self.width + self.length) * 2    
    
    def color(self):
        return str(self.c).title() 

arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else: print("INVALID")
