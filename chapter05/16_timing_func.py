import time

def get_time(num):
    start_time = time.time()
    #calculations
    result = sum(range(num))
    end_time = time.time()
    print(f"Function took {end_time - start_time} seconds to run!")
    return result

def main():
    print(get_time(1_000_000))

if __name__ == "__main__":
    main()