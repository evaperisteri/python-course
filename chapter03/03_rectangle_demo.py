def is_square(length: int, width: int) -> bool:
    """
    Checks if a rectangle is a square.
    Args:
        length(int): the length of the rectangle.
        width(int): the width of the rectangle.
    Returns:
        bool. True if the rectangle is square, false otherwise
    """
    return length == width

def main():
    try:
        length = int(input("Enter the length of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))
        if is_square(length, width):
            print("The rectangle is square!")
        else:
            print("The rectangle is not square :(")
    except ValueError:
        print("invalid input. please enter two integers")
    

if __name__ == "__main__":
    main()