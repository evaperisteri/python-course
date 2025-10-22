def calculator(n1, n2, operation):
    try:
        return operation(n1, n2)
    except TypeError as e:
        print(f"Error: {e}. Ensure the 'operation' argument is a function which takes 2 ints as args.")

def add(no1, no2):
    return no1 + no2

def mul(no1, no2):
    return no1 * no2

def main():
    print("Addition:", calculator(7, 9, add))
    print("Multiplication:", calculator(40, 100, mul))

if __name__ == "__main__":
    main()