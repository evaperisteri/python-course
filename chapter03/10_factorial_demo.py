def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main():
    try:
        n = int(input("Please insert an integer: "))
        if n < 0:
            raise ValueError
    except ValueError:
        print("Invalid input, please insert a positive integer")
    
    facto = calculate_factorial(n)
    print(f"{n}! = {facto}")

if __name__ =="__main__":
    main()