#In Python, name mangling is a mechanism that protects class and instance attributes from being accidentally overridden or accessed from outside the class. it renames __y = _Point__y
class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self.__y = y

    def __str__(self):
        return f"({self._x}, {self.__y})"

def main():
    p1 = Point(10, 20)
    print(p1)
    
    #print(p1.__x)
    print(p1._x)
    #p1.__y = 100 θετουμε τιμη σε μια "αλλη" μεταβλητη, όχι στο y του p1
    print(p1.__y)
    #print(p1.__y)
    #print(p1._Point__y)

if __name__ == "__main__":
    main()