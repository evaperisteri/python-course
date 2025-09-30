def get_average(*numbers):
    """
    ...
    """
    if not numbers:
        return "No numbers provided"
    average = sum(numbers) / len(numbers)
    return"{:.2f}".format(average)


def main():
    nums= [10, 20, 30, 40]

    #my_average = get_average(*nums)
    #my_average = get_average(nums) χωρις το * δεν λειτουργεί διότι περιμένει να λάβει τα στοιχεία ενος  Itterable object, unpacked
    my_average = get_average(10, 20, 30, 40)
    print(my_average)

if __name__ == "__main__":
    main()