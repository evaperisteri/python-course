import functools
# from functools import reduce

def calculate(args):
    def plus():
        """return the sum of the numbers"""
        return functools.reduce(lambda x, y: x + y, args)

    def minus():
        """return the sustruction of the numbers"""
        return functools.reduce(lambda x, y: x - y, args)
    
    def mul():
        return functools.reduce(lambda x, y: x * y, args)
    
    def div():
        # if not 0 in args[1:]
        return args[0]/sum(args[1:])
    
    return plus, minus, mul, div
    
def main():
    list_of_ints = [26, 5, 4, 3, 2, 1]
    plus_func, minus_func, mul_func, div_func = calculate(list_of_ints)
    print(f"plus_func: {plus_func()}")
    print(f"minus_func: {minus_func()}")
    print(f"mul_func: {mul_func()}")
    print(f"div_func: {div_func()}")

if __name__ =="__main__":
    main()