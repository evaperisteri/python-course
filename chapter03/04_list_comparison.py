def compare_lists(list1, list2):
    """
    Compares two lists for identity and equality.
    Args:
        list1(list): The first list to compare.
        list2(list): The second list to compare.
    Return:
        None
    """
    #identity check ---> list1 is list2
    print(f"{list1} and  {list2} are identical: {list1 is list2}")

    #equality check ---> list1 == list2
    print(f"{list1} == {list2} are equal: {list1 == list2}")

def main():
    my_list = [1, 2, 3]
    your_list = [1, 2, 3]

    #compare lists
    compare_lists(my_list, your_list)
    print(id(my_list))
    print(id(your_list))

if __name__ == "__main__":
    main()