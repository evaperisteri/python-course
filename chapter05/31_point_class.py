class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.__x + other.__x, self.__y + other.__y)
        elif isinstance(other, (int, float)):
            return Point(self.__x + other, self.__y +other)
        else:
            raise TypeError("unsupported operand types for point")

    def __radd__(self, other):
        return self.__add__(other)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.__x == other.__x and self.__y==other.__y
        else:
            return False

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y = value

def do_add(a, b):
    return a + b

def main():
    p1 = Point(1, 2)
    p2 = Point(3, 4)

    print(f"p1: {p1}")
    print(f"p2: {p2}")
    print(f"p1 + p2 = {p1 + p2}")
    print(f"p1 + 10 = {p1 + 10.2}")
    #p2.x = 1 
    #p2.y = 2 we get true at the next equation
    print(f"p1 == p2 : {p1 == p2}")
    print(f"10 + p1 : {10 + p1}") #-> type error: we need radd

if __name__ == "__main__":
    main()