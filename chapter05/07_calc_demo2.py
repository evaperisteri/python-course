import functools
# from functools import reduce

def calculate(args):
    def plus():
        """return the sum of the numbers"""
        return functools.reduce(lambda x, y: x + y, args)

    def minus():
        """return the sustraction of the numbers"""
        return functools.reduce(lambda x, y: x - y, args)
    
    def mul():
        return functools.reduce(lambda x, y: x * y, args)
    
    def div():
        # if not 0 in args[1:]
        return args[0]/sum(args[1:])
    
    return {"add":plus, "substract":minus, "multiply":mul, "division":div}
    
def main():
    list_of_ints = [26, 5, 4, 3, 2, 1]
    operations = calculate(list_of_ints)
    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Substraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
            choice = int(input("enter a number between 1 and 5: "))
        except ValueError:
            print("Invalid input")
            continue

        match choice:
            case 1:
                print("Addition:", operations["add"]())
            case 2:
                print("Substraction:", operations["substraction"]())
            case 3:
                print("Multiplication:", operations["multiply"]())
            case 4:
                print("Division:", operations["division"]())
            case 5:
                print("Goodbye")
                break
            case _:
                print("Invalid input. please try again")

if __name__ =="__main__":
    main()