class FactoIterator:
    def __init__(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        self.n=n
        self.result = 1
        self.order = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.order > self.n:
            raise StopIteration
        
        if self.order == 0:
            self.order += 1
            return 1
        self.result *= self.order
        self.order += 1
        return self.result
    
def main():
    facto_iter = FactoIterator(10) # here we call init(the constructor) not the iterator
    #get the first factorial using next() func
    # thats why here with next we get only the first facto. the iteration is not consumed yet
    # (next() calls __next__() once, getting only the first factorial (1! = 1), and the iterator state advances but isn't fully consumed.)
    a = next(facto_iter)
    print(a)

    for facto in facto_iter:
        print(facto)

    print("------------")

    new_facto_iter = FactoIterator(5)
    for index, factorial in enumerate(new_facto_iter, start=1):
        print(f"Factorial of {index} = {factorial}")
if __name__ == "__main__":
    main()