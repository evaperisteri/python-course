def test_args_func(pos_arg1, pos_arg2, opt_arg1 = None, opt_arg2 = None, *args, **kwargs):
    """
    Function to demonstrate the usage of positional, optional, additional optional(*args) 
    and additional keyword arguments(**kwargs).
    Parameters:
        pos_arg1 (Any): The first positional argument.
        pos_arg2: The second positional argument.
        opt_arg1: The first optional argument. Defaults to None.
        opt_arg2: The second optional argument. Defaults to None.
        *args: Additional positional arguments.
        **kwargs: Additional keyword arguments.
    Notes:
        - Positional arguments must be provided in the correct order
        - Optional arguments can be skipped or provided in order
        - Use keyword syntax for optional arguments when skipping earlier ones
        - *args collects all additional positional arguments into a tuple
        - *args collects EXTRA POSITIONAL arguments after all defined parameters are filled
        - Optional arguments (opt_arg1, opt_arg2) are filled BEFORE *args gets any values
        - **kwargs collects all additional keyword arguments into a dictionary
    """
    # Print positional arguments
    print("Pos arg1:", pos_arg1)
    print("Pos arg2:", pos_arg2)

    # Print optional arguments
    print("Opt arg1:", opt_arg1)
    print("Opt arg2:", opt_arg2)

    # Print Additional pos args
    if args:
        print("Additional pos args: ")
        for arg in args:
            print(arg)

    if kwargs:
        print("Additional keyword args: ")
        for key, value in kwargs.items():
            print(f"{key}:{value}")

def main():
    test_args_func("Hello", "cf7") # Pos arg1:Hello Pos arg2:cf7 Opt arg1: None Opt arg2 :None
    test_args_func("Hello", "cf7", 100) # Pos arg1:Hello Pos arg2:cf7 Opt arg1: 100 Opt arg2 :None
    test_args_func("Hello", "cf7", 100, 200) # Pos arg1:Hello Pos arg2:cf7 Opt arg1: 100 Opt arg2 :200
    print("---------------------")
    test_args_func("Hello", "cf7", opt_arg2=100)  # Pos arg1:Hello Pos arg2:cf7 Opt arg1: None Opt arg2 :100
    test_args_func("Hello", "cf7", name="Eva", age=101) # Pos arg1:Hello | Pos arg2:cf7 | Opt arg1: None | Opt arg2 :None | Additional keyword args | name:Eva | age:101
    test_args_func("Hello", "cf7",                              #positional arg 1 & 2
                    100, 200,                                   #optional arg 1 & 2
                    300, "Bob",                                 # *args
                    name = "Eva", street = "Coding"             #**kwargs
    )

'''
Pos arg1: Hello
Pos arg2: cf7
Opt arg1: 100
Opt arg2: 200
Additional pos args
300
Bob
Additional keyword args
name:Eva
street:Coding
'''

if __name__ == "__main__":
    main()