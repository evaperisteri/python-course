class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        if not hasattr(self, '_name'):
            return "name attribute is deleted"
        print("getting name")
        return self._name
    
    def set_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be string")
        print("setting name...")
        self._name = value

    def del_name(self):
        print("deleting name...")
        del self._name
    name = property(get_name, set_name, del_name, "this is the 'name' property")

def main():
    p = Person("Nick")
    print(p.name)
    p.name = "John"
    print(p.name)
    del p.name
    print(p.name)
    p.friends = [] # Linter warning: "Instance attribute defined outside __init__"
    p.friends.append("Chris")
    p.friends.append("Ioannis")
    print("friend list:")
    for friend in p.friends:
        print(f" - {friend}")


if __name__ == "__main__":
    main()