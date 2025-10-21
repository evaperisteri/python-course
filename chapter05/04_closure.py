def department_id_generator(department):
    """
    Factory function that creates ID generators for different departments.
    
    Theory: This demonstrates CLOSURES in Python - a function that remembers 
    values in enclosing scopes even when they are not present in memory.
    """
    last_id = 0
    def generate_id():
        """
        Inner function that maintains state between calls.
        
        Theory: This is a CLOSURE - it captures and remembers the 'last_id' 
        variable from the enclosing scope, creating persistent state.
        """
        nonlocal last_id  # Needed to modify the captured variable from outer scope
        last_id += 1
        return f"{department}-{last_id}", last_id
    return generate_id

def main():
    """
    Demonstrates multiple independent closures maintaining separate states.
    
    Theory: Each call to department_id_generator() creates a NEW closure 
    with its OWN state. This is an alternative to using classes for 
    maintaining state between function calls.
    """
     # Create two independent generators - each has its own state
    python_id_gen = department_id_generator("Python")
    android_id_gen = department_id_generator("Android")
    # print(python_id_gen()) -> unbound local error: cannot access local variable 'last_id' so we added nonlocal in front of the variable last id
    # Theory: Each closure maintains separate 'last_id' state
    print(python_id_gen()) #('Python-1', 1)
    print(python_id_gen())

    print(android_id_gen())
    print(android_id_gen())


if __name__ == "__main__":
    main()