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

if __name__ == "__main__":
    main()