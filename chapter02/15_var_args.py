#Variable-length arguments, varargs for short, are arguments that can take an unspecified amount of input.
def print_cities(*cities): #*: mporeis na eisageis mia, kamia h perissoteres apo mia times
    if not cities:
        print("No cities provided")
    else:
        print("Cities:", ", ".join(cities))

def main():
    print_cities()
    print_cities("Athens") #katalabainei to join oti sti mia timh den prepei na balei ton diaxwristi
    print_cities("Athens", "London", "Paris")


if __name__ =="__main__":
    main()