def is_armstrong_number(n): # 153
    digits = str(n)
    power = len(digits)
    total = 0

    #'1', '5', '3'
    for digit in digits:
        total += int(digit) ** power

    return n == total

def main():
    try:
        n = int(input("Please insert an integer: "))
    except ValueError:
        print("Invalid input")
        return

    if is_armstrong_number(n):
        print(f"{n} is an Armstrong number")
    else:
        print(f"{n} is not an Armstrong number")

if __name__ == "__main__":
    main()