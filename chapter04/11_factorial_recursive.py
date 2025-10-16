def factorial(n: int) -> int:
    """
    Calculates the factorial of a non-negative integer n using recursion.
    Factorial definition:
        n! = n × (n−1)!
    Base cases: 0! = 1, 1! = 1
    Returns:
        int: The factorial of n.
             Returns 0 if n is negative (invalid input).
    """
    # Base cases: 0! = 1, 1! = 1
    if n < 0: return 0
    if n in (0,1): return 1
    return n * factorial(n-1)

def main():
    n= int(input("Please enter an integer: "))
    print(f"{n}! = {factorial(n)}")

if __name__ =="__main__":
    main()