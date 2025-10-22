from collections import deque

def display_garage(garage: deque) -> None:
    if garage:
        print("Current cars in the garage:")
        for position, car in enumerate(garage, 1):
            print(f"{position}. {car}")
    else:
        print("The garage is empty.")

def add_car_to_garage(garage: deque, max_capacity: int)->None:
    if len(garage) < max_capacity:
        car_name = input("Enter the name or ID of the car: ")
        garage.append(car_name)
        print(f"{car_name} has entered the garage")
    else:
        print("the garage is full. Cannot add more cars")

def remove_car_from_garage(garage: deque)->None:
    if garage:
        car_left = garage.popleft()
        print(f"{car_left} has left the garage")
    else:
        print("Garage is empty. No cars to be removed.")

def main():
    garage = deque()  # Create a deque to represent the garage
    max_capacity = 5  # Maximum number of cars the garage can hold

    while True:
        print("\nOptions:")
        print("1. Add a car ")
        print("2. Remove the first car from the garage")
        print("3. Display the garage state")
        print("4. Exit")

        try:
            choice = int(input("Select an option (1-4): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue

        match choice:
            case 1:
                add_car_to_garage(garage, max_capacity)

            case 2:
                remove_car_from_garage(garage)

            case 3:
                display_garage(garage)

            case 4:
                print("Exiting the program. Goodbye!")
                break

            case _:
                print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()