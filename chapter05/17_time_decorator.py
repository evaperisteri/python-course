import time

def timer_decorator(func):
    """
    Decorator to measure the rexecution time of a function.
    Params:
        func(function): The function to ne decorated
    Returns:
        function: the decorated function with added timing functionality.
    """
    def inner_function(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to run")
        return result
    return inner_function

def sum_function(n):
    return sum(range(n))

@timer_decorator
def average_function(n):
    if n ==0:
        return 0
    total_sum = sum(range(n))
    return total_sum / n


def main():
    my_sum_func = timer_decorator(sum_function)
    print(my_sum_func(1000000))
    print(average_function(101))

if __name__ == "__main__":
    main()