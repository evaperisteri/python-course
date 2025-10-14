from typing import List, Any

my_list = [1, 2, "Hello", [3, 4, 5]]

def append_to_list(li: List[Any], element: Any) -> None:
    li.append(element)

def main():
    append_to_list(my_list, "CF")
    for item in my_list:
        print(item, end=" ")
    print()

if __name__ == "__main__":
    main()