from typing import Sequence, TypeVar, List, Any, Optional

# A generic type variable
T = TypeVar('T')

Number = TypeVar('Number', int, float)

# first()
def first(seq: Sequence[T]) -> T:
    """
    Returns the first element of a sequence.
    if sequense is empty, raises a Value Error.
    Args:
        seq (Sequence[T]): The sequence from witch to get the first element.
    Returns:
        T: The first element of a sequence.
    """
    if not seq:
        raise ValueError("Sequence is empty.")
    return seq[0]
def last(seq: Sequence[T]) -> T:
    """
    Returns the last element of a sequence.
    if sequense is empty, raises a Value Error.
    Args:
        seq (Sequence[T]): The sequence from witch to get the last element.
    Returns:
        T: The last element of a sequence.
    """
    if not seq:
        raise ValueError("Sequence is empty.")
    return seq[-1]

def count_truthy(elements: List[Any]) -> int:
    """
    Counts how many elements in the list are truthy
    Args:
        elements (List[Any]): A list of elements.
    Returns:
        int: count of truthy elements in the list
    """
    return sum(1 for element in elements if element)

def len_str(s: Optional[str] = None) -> int:
    return len(s) if s is not None else 0

def main():
    numbers = [10, 20, 30, 40, 50]
    print(f"First number: {first(numbers)}")
    print(f"Last number: {last(numbers)}")

    try:
        print("First element of []:", first([]))
    except ValueError as e:
        print(e)

    mixed_values = [0, True, False, 'Hello', '', None, 17]
    print("Truthy Values are:", count_truthy(mixed_values))
    print("Length of 'Hello World':", len_str('Hello World'))
    print("Length 'None':", len_str(None))
    print(first("Hello CF!"))
if __name__ == "__main__":
    main()