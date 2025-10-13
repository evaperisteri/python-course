def name_space(num: int):
    if not isinstance(num, int): #(object, class)
        print("The num must be integer.")
        return
    if num < 0:
        print("The num must be positive.")
        return
    
    name = input("Please enter your name: ").strip() #removes white spaces

    if not name:
        print("No name provided")
        return
    
    spaced_name = (" " * num).join(name)
    print(spaced_name)

def main():
    try:
        num = int(input("Enter the number of spaces between the characters: "))
        name_space(num)
    except ValueError:
        print("Invalid input...")

if __name__ == "__main__":
    main()