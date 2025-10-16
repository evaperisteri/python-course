def fibo(n: int) -> int:
    """
    Definition:
        The Fibonacci sequence is a series of numbers in which
        each number (after the first two) is the sum of the two preceding ones.

        Sequence example:
            0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

        Mathematically:
            fibo(0) = 0
            fibo(1) = 1
            fibo(n) = fibo(n-1) + fibo(n-2)  for n > 1

    This implementation uses recursion:
        It calls itself with smaller values of n until
        it reaches the base cases (0 and 1).

    Parameters:
        n (int): A non-negative integer indicating the position
                 in the Fibonacci sequence.

    Returns:
        int: The n-th Fibonacci number.

    Note:
        This recursive version is simple but inefficient for large n,
        because it recalculates many intermediate values multiple times.
    """
    # fibo(n) = fibo(n-1) + fibo(n-2)
    # fibo(0) = 0
    # fibo(1) = 1

    if n in (0,1): return n
    return fibo(n-1)+fibo(n-2)

def main():
    n = int(input("Please enter a possitive integer: "))
    print(f"fibo({n}) = {fibo(n)}")

if __name__ == "__main__":
    main()