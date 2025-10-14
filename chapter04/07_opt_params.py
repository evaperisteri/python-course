# ->Positional parameters:
# Values are assigned by their position in the call.
# Example: add(10, 20) → a=10, b=20, c=30 (default).

# ->Optional (default) parameters:
# Have a default value in the function definition, so you can omit them.
# Example: b=20, c=30 in add().

# ->Keyword arguments:
# You explicitly name which parameter you’re setting, e.g. add(100, c=50).

def add(a:int, b:int = 20, c:int = 30) -> int:
    """
        Demonstrates positional and optional (default) parameters.
        
        Parameters:
            a (int): Required positional argument (must be provided).
            b (int): Optional argument with a default value of 20.
            c (int): Optional argument with a default value of 30.
            
            If b or c are not provided, their default values are used.
    """
    return a + b + c


def full_optional_add(a:int = 0, b:int = 0, c:int = 0):
    """
    All parameters are optional because they have default values.
    You can call this function with any combination of arguments
    (positional or keyword).
    """
    return a + b + c

def main():
    # In this call, a=10 (positional), b=20 (positional), c uses default (30)
    print(add(10, 20)) 
    # All arguments provided positionally: a=100, b=50, c=30 (default)
    print(add(100, 50))
    # Mix of positional and keyword: a=100 (positional), c=50 (keyword)
    # b uses its default (20)
    print(add(100, c=50))
    # All parameters passed as keywords, order doesn’t matter
    print(full_optional_add(c = 3, a = 10, b = 4))

if __name__ == "__main__":
    main()