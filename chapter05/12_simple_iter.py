class SimpleIterator:
    #constructor
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
        
def main():
    numbers = [10, 20, 30, 40, 50]

    # create an unstance of simpleIterator (an iterator)
    my_iter = SimpleIterator(numbers)
    a = next(my_iter)
    print(a)
    print("------")
    for item in my_iter:
        print(f"item: {item}")

if __name__ == "__main__":
    main()