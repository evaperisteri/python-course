# yield: converts a simple function into a generator
# returns a generator object

def simple_generator():
    print("first value")
    yield 1
    print("second value")
    yield 2
    print("third value")
    yield 3

def main():
    gen = simple_generator()

    print(next(gen))
    print("-------------")
    print(next(gen))
    print(next(gen))

if __name__ == "__main__":
    main()