import re #regular expressions

#initialize my stack --last in first out
stack = []

num = 0

def push(list, item):
    list.append(item)

def pop(list):
    if list:
        return list.pop()
    else:
        print("Stack is empty")

def print_stack(list):
    if list:
        print("Current state:", list)
    else:
        print("Stack is empty")

def print_menu():
    print("1. Insert on top")
    print("2. Get from the top")
    print("3. Print stack")
    print("4. q/Q for Quit")

def get_choice():
    return input("Please provide your choice\n") #epistrefei string logw tis input

def main():
    choice = 0
    num = 0
    out_num = 0

    while True:
        print_menu()
        choice = get_choice() 

        if not choice:
            continue

        if choice == 'q' or choice == 'Q':
            break

        pattern = r'^\d$'
        valid = re.match(pattern, choice)

        if not valid:
            print("Error in choice")
            continue

        choice = int(choice)

        #python 3.10 +: peripou san tin switch case
        match choice:
            case 1:
                num = input("Please insert a number: ") #num:string
                pattern = r'^\d+$' #θετικος ακεραιος
                valid = re.match(pattern, num)

                if not valid:
                    print("Error")
                    continue

                num = int(num)
                #push on stack
                push(stack, num)
                print(f"{num} inserted.")

            case 2:
                out_num = pop(stack)
                if out_num is not None:
                    print(f"{out_num} removed.")

            case 3:
                print_stack(stack)
            
            case _:  #default case in java
                print("Not a valid choice")



if __name__ == "__main__":
    main()