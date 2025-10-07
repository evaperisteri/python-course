def compare_integers(a, b):
    if a == b:
        print("the numbers are equal.")
    elif a > b:
        print("the first number is greater than the second number")
    else:
        print("The first number is smaller than the second number")

def main():
    try:
        a = int(input("please enter the first number: "))
        b = int(input("please enter the second number: "))
    except ValueError:
        print("invalid input.")
        return
    
    compare_integers(a, b)

    # 1. simple example (ternary operator)
    if a >0:
        print("positive")
    else:
        print("non-positive")

    #print("positive" if a > 0 else "non-positive") 
    result = "positive" if a > 0 else "non-positive"
    print(result)

    # 2. extended example (ternary operator) 
    result = (
        "The numbers are equal." if a == b else
        "The first number is greater than the second number." if a > b else
        "The first number is smaller than the second number."
    )
    
    print(result)

if __name__ == "__main__":
    main()