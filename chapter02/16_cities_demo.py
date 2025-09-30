def print_cities(*cities, sep = ", ", my_end="\n"): 
    """
    Print a list of cities separated by a specified separator and ending with a specified end character.
    
    Parameters:
        *cities(str): Cities witch are going to be printed
        sep(str): Separator between city names. Default is ', '
        end(str): End character after the last city. Default is '\n'
    """
    if not cities:
        print("No cities provided", end=my_end)
    else:
        print("Cities:", sep.join(cities), end=my_end)

def main():
    print_cities()
    print_cities("Athens")
    print_cities("Athens", "London", "Paris")
    print("-------------------")
    print_cities("Athens", "Paris", "London", "Patras", sep=" | ", my_end=".")
    print("\n------------------------")

if __name__ =="__main__":
    main()