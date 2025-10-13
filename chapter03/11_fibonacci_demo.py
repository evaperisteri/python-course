def main():
    n = int(input("Please insert an integer: "))
    a = 0
    b = 1

    for i in range(2, n + 1):
        temp = a
        a = b
        b = temp + b

    print(f"The {n}th Fibo number is: {b}")

if __name__ =="__main__":
    main()