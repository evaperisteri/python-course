def fibonacci(n):
    # if n == 0: return 0
    # if n == 1: return 1
    if n in (0, 1): return n

    # a = 0
    # b = 1
    a, b = 0, 1

    # temp = a
    # a = b
    # b = temp + b
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b 

def main():
   pass

if __name__ =="__main__":
    main()